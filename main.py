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

@app.get("/api/v1/users")
def get_users():
    return db

@app.post("/api/v1/users")
def create_user(user:Usuario):
    userObject = {**user.dict(),"id":uuid4()}
    db.append(userObject)
    return {"message":"User created sucessfully","data":user}

@app.get("/api/v1/users/{user_id}")
def get_user(user_id:int):
    if user_id > len(db):
        return db[user_id]
    return {"message":"User not found"}

@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id:int):
    result = userExists(db,user_id)
    if(result[0]):
        del db[user_id]
        return {"message":"User deleted sucessfully!","data":}
    
    if(len(db)>user_id):
        user_deleted = db[user_id]
        del db[user_id]
        return {"message":"User deleted successfully","data":user_deleted}
    return {"message":"User not found!"}

@app.put("/api/v1/users/{user_id}")
def update_user(user_id: int,usuario: Usuario):
    if user_id < len(db):
        db[user_id] = usuario
        return{
            "message":"User updated sucessfully",
            "data":usuario
        }
    return {"message":"User not found"}
