from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    
    
class UsuarioRead(BaseModel):
    id: int
    nome: str
    
    class config:
        from_attributes = True  
    