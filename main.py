""""
    Modulo principal de la aplicacion FastAPI para la gestion de usuarios.
"""


from typing import List, Union
from uuid import uuid4
from fastapi import FastAPI
from model import Genero,Usuario,Role, UsuarioUpdate
from functions import user_exists, get_user_index

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Jesús",
        apellidos="Domínguez Ramírez",
        genero=Genero.MASCULINO,
        roles=[Role.USER]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Miranda",
        apellidos="Castillo Ibarra",
        genero=Genero.FEMENINO,
        roles=[Role.USER]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Ivan",
        apellidos="Yau Hong",
        genero=Genero.OTRO,
        roles=[Role.USER]
    )
]

app = FastAPI()

@app.get("/health")
def health_check():
    """Endpoint para verificar el estado de la aplicacion"""
    return {"status":"Active!"}

@app.get("/api/v1/users")
def get_users():
    """Endpoint para obtener todos los usuarios"""
    return db

@app.post("/api/v1/users")
def create_user(user:Usuario):
    """Endpoint para crear un nuevo usuario"""
    new_user = Usuario(**user.dict(),id=uuid4())
    db.append(new_user)
    return {"message":"User created sucessfully","data":new_user}

@app.get("/api/v1/users/{user_id}")
def get_user(user_id:Union[int,str]):
    """Endpoint para obtener un usuario por su ID"""
    result = user_exists(db,user_id)

    if result[0]:
        return db[get_user_index(db,user_id)]

    return {"message":"User not found"}

@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id:Union[int,str]):
    """Endpoint para eliminar un usuario por su ID"""
    exists , _ = user_exists(db,user_id)

    if exists:
        del db[get_user_index(db,user_id)]
        return {"message":"User deleted sucessfully!","data":str(user_id)}

    return {"message":"User not found!"}

@app.put("/api/v1/users/{user_id}")
def update_user(user_id: Union[int,str],usuario: UsuarioUpdate):
    """Endpoint para actualizar un usuario por su ID"""
    index = get_user_index(db,user_id)
    if index != -1:
        db[index] = usuario
        return{
            "message":"User updated sucessfully",
            "data":usuario
        }
    return {"message":"User not found"}
