from fastapi import FastAPI
from pydantic import BaseModel
import docker
import os
import subprocess


client = docker.from_env()

app = FastAPI()  

script = "./script"

comandodocker = "sudo docker run python python -c "

class Item(BaseModel):
    message: str

@app.get("/") 
async def root():
    return {"message": "Hello World"}

@app.get("/tasks")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/post") 
async def post(item: Item):
    msg = item.message
    msg = msg.replace('/', '"')
    print(msg)
    prog = open("helloword.py", "w")
    prog.write(msg)
    prog.close() 
    try:
        dock = os.popen(comandodocker+msg)
    except:
        print('erro')

    result = dock.read()
    print(result)

    return {"mensagem": result}

