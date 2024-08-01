
import sys
import threading
import time

import uvicorn
from fastapi import FastAPI, Request, Response, status, Body
from passlib.context import CryptContext

from petdb import PetDB, PetCollection, PetArray
from petdb.service.qlock import QLock

if sys.platform != "linux":
	raise Exception("PetDB.service supports only Linux system")

STORAGE_PATH = "/var/lib/petdb"

db = PetDB.get(STORAGE_PATH)
app = FastAPI()
crypt = CryptContext(schemes=["pbkdf2_sha256"], default="pbkdf2_sha256")
lock = QLock()

@app.post("/collections")
def get_collections():
	with lock:
		return db.collections()

@app.post("/drop")
def drop_collections():
	with lock:
		db.drop()

@app.post("/drop/{name}")
def drop_collection(name: str):
	with lock:
		db.drop_collection(name)

@app.post("/mutate/{name}")
def mutate(name: str, mutations: list[dict] = Body(embed=True)):
	with lock:
		array = db.collection(name)
		for mutation in mutations:
			array: PetArray = array.__getattribute__(mutation["type"])(*mutation["args"])
		return array.list()

@app.post("/insert/{name}")
def insert(name: str, doc: dict = Body(embed=True)):
	with lock:
		return db.collection(name).insert(doc)

@app.post("/insert_many/{name}")
def insert_many(name: str, docs: list[dict] = Body(embed=True)):
	with lock:
		return db.collection(name).insert_many(docs)

@app.post("/update_one/{name}")
def update_one(name: str, update: dict = Body(embed=True), query: dict = Body(embed=True)):
	with lock:
		return db.collection(name).update_one(update, query)

@app.post("/update/{name}")
def update(name: str, update: dict = Body(embed=True), query: dict = Body(embed=True)):
	with lock:
		return db.collection(name).update(update, query)

@app.post("/remove/{name}")
def remove(name: str, query: dict = Body(embed=True)):
	with lock:
		return db.collection(name).remove(query)

@app.post("/clear/{name}")
def clear(name: str):
	with lock:
		return db.collection(name).clear()

def cache_monitor():
	while True:
		print("start cache checking...")
		now = int(time.time())
		with lock:
			instances = PetCollection.instances()
			for path in list(instances.keys()):
				print(f"check {instances[path]["instance"].name}...")
				if now - instances[path]["created"] > 3 * 24 * 3600:
					print(f"clear {instances[path]["instance"].name}")
					del instances[path]
		time.sleep(24 * 3600)

def run(port: int = 3944, password_hash: str = ""):

	@app.middleware("http")
	async def authentication(request: Request, call_next):
		body = await request.json()
		if crypt.verify(body["password"], password_hash):
			return await call_next(request)
		return Response(status_code=status.HTTP_401_UNAUTHORIZED)

	threading.Thread(target=cache_monitor).start()

	uvicorn.run(app, host="127.0.0.1", port=port)
