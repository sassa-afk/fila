from fastapi import APIRouter, HTTPException, Query
from typing import Optional


router = APIRouter()

minhaFila = None  

def set_fila(fila):
    global minhaFila
    minhaFila = fila

 
auth = None 

def set_auth(security):
    global auth
    auth = security
    

# http://localhost:5000/fila/tamanho
@router.get("/fila/tamanho" ,
     summary="Mostra tamanho geral da fila (Não utiliza autenticação)",
    description="Retorna o tamanho da fila atual",
)
def read_fila_tamanho():
    return {"message": minhaFila.tamanhoFila()}

# http://localhost:5000/fila/verFila
@router.get("/fila/verFila",
     summary="Consulta todos que estão na fila (Não utiliza autenticação)",
    description="Retorna todos que entraram na fila com dados de prioridade, identificação , posição e senha .",
)
def read_fila_verFila():
    return {"message": minhaFila.verFila()}


#http://localhost:5000/fila/posicaoFila?"senha"
@router.get("/fila/posicaoFila",
     summary="Consulta posição de uma senha na fila (Não utiliza autenticação)",
    description="Recebe a senha do cliente e retorna sua posição atual na fila.",
)

def read_fila_posicaoFila(senha: Optional[str] = Query(default=None)):
    if not senha:
        raise HTTPException(status_code=400, detail="Parâmetro inválido")
    pos = minhaFila.posicaoFila(senha)
    if pos is None:
        raise HTTPException(status_code=404, detail="Senha não encontrada")
    return {"message": f"Senha identificada na posição {pos}"}
    
    

