from model import Usuario
from typing import List
def userExists(db:List[Usuario],user_id:str) -> bool:
    for idx,user in db:
        if user.id==user_id:
            return [True,idx]
    return [False,False]