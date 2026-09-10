from pydantic import BaseModel

class TransacaoCreate(BaseModel):
    descricao: str
    valor: float
    categoria_id: int
    usuario_id: int
    
class TransacaoRead(BaseModel):
    id: int
    descricao: str
    valor: float
    categoria_id: int
    usuario_id: int
    
    class Config:
        from_attributes = True  