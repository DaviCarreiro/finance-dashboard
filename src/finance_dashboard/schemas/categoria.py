from pydantic import BaseModel
class CategoriaCreate(BaseModel):
    nome: str
    
class CategoriaRead(BaseModel):
    id: int
    nome: str
    
    class Config:
        from_attributes = True