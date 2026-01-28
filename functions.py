""" Módulo de funciones auxiliares para la gestión de usuarios """

from typing import List, Union, Tuple
from model import Usuario

def user_exists(db:List[Usuario],user_id:Union[int,str]) -> Tuple[bool,Union[str,bool,int]]:
    """ Función para verificar si un usuario existe en la base de datos por su ID """
    for user in db:
        if str(user.id)==str(user_id):
            return True,user.id
    return False,False

def get_user_index(db:List[Usuario],user_id:Union[int,str]) -> int:
    """ Función para obtener el índice de un usuario en la base de datos por su ID """
    for index,user in enumerate(db):
        if str(user.id)==str(user_id):
            return index
    return -1
