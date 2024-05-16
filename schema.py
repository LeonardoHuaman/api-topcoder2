from pydantic import BaseModel
class Item (BaseModel):
    
    id : int
    nombres : str
    apellidos : str
    ciudad : str
    correo : str
    tc_name : str
    
    