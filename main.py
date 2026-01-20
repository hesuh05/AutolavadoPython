from typing import List, Optional, Union;
from uuid import UUID, uuid4;
from model import Genero,Usuario,Role;

from fastapi import FastAPI

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Jesús",
        apellidos="Domínguez Ramírez",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Miranda",
        apellidos="Castillo Ibarra",
        genero=Genero.femenino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Ivan",
        apellidos="Yau Hong",
        genero=Genero.otro,
        roles=[Role.user]
    )
]

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"Active!"}

@app.get("/items/item/{item_id}")
def read_item(item_id:int, q: Union[int,str]=None):
    return {"item":items[item_id],"query":q}

@app.get("/api/v1/users")
def get_users(user_id:int):
    return db

@app.get("/api/v1/users/{user_id}")
def get_user(user_id:int):
    return db[user_id]

@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id:int):
    if(len(db)>user_id):
        user_deleted = db[user_id]
        del db[user_id]
        return {"message":"User deleted successfully","data":user_deleted}
    return {"message":"User not found!"}

@app.put("/api/v1/users/{user_id}")
def update_user(user_id,Usuario):
    return {}
