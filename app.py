from fastapi import FastAPI
from pydantic import BaseModel
import docker
import os
import subprocess


client = docker.from_env()

app = FastAPI()  

script = "./script"


class Item(BaseModel):
    message: str

@app.get("/") 
async def root():
    return {"message": "Hello World"}

@app.get("/tasks/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/tasks/{item_id}") 
async def post(item_id: int, item: Item):
    msg = item.message
    print(msg)
    #prog = open("helloword.py", "w")
    #prog.write(msg)
    #prog.close()
    comando = "sudo docker run python python -c " + msg
    try:
        stream = os.popen(comando)
    except:
        print('erro')
    output = stream.read()
    file = "./result.txt"
    with open(file, 'r') as result:
        result = result.read()
        print(output)
    return {"mensagem": result, "item_id": item_id}

