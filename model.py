"""
    Modelo de datos para la aplicación de gestión de usuarios.
"""

from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Genero(str,Enum):
    """ Definición de géneros posibles """
    MASCULINO="Hombre"
    FEMENINO="Mujer"
    OTRO="Otro"

class Role(str,Enum):
    """ Definición de roles posibles """
    ADMIN = "admin"
    USER = "user"
    INVITADO = "invitado"

class Usuario(BaseModel):
    """ Modelo de usuario con atributos básicos """
    id: Optional[UUID] = uuid4()
    primerNombre:str
    apellidos:str
    genero:Genero
    roles:List[Role]

### SECCION DE AUXILIARES PARA POST

class UsuarioUpdate(BaseModel):
    """ Modelo para actualizar un usuario con atributos opcionales """
    primerNombre: Optional[str] = None
    apellidos: Optional[str] = None
    genero: Optional[Genero] = None
    roles: Optional[List[Role]] = None
