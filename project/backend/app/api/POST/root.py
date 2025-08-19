from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import random, string
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from app.core.security import auth_token
 
router = APIRouter()

 
minhaFila = None  
auth = None

 
def set_fila(fila):
    global minhaFila
    minhaFila = fila

def set_auth(security):
    global auth
    auth = security

 
class Item(BaseModel):
    prioridade: int
    identidade: str
    
 
# curl -X POST http://localhost:5000/fila/chamarNormal   -H "Authorization: Bearer "

# -----------------------
# Rotas
# -----------------------

#http://localhost:5000/fila/entrar
@router.post("/fila/entrar",
     summary="Entrar na fila (Não utiliza autenticação)",
    description="Possibilitar entrar na fila com informações no body de identificação ( valor string  nome ou cpf) , prioridade (int onde 1 é  a principal d) e gerar uma senha aleatoria ",
)

def entrar_fila(item: Item):
    if not item.prioridade or not item.identidade:
        raise HTTPException(status_code=400, detail="Body incompleto")
    senha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    pos = minhaFila.add(senha, item.prioridade, item.identidade)
    return {"message": f"Senha {senha} adicionada na posição {pos}"}
    
    
  #------------  -----------------
  
#http://localhost:5000/fila/newToken
 

@router.post(
    "/fila/newToken",
    summary="Gerar novo token JWT (Não utiliza autenticação)",
    description="""
Utilizado para gerar um token JWT para realizar procedimentos específicos de chamar pessoas na fila.
Caso não apareça a opção para realizar a requisição no Swagger, tente o curl:

curl -X POST http://localhost:5000/fila/newToken \
-H "Content-Type: application/json" \
-d '{"ident": "identificação"}'
""",)
async def new_token(request: Request):
    body = await request.json()
    if "ident" not in body or not body["ident"]:
        raise HTTPException(status_code=400, detail="Body incompleto")
    token = auth.new_token(
        dados={"user": body["ident"]}, 
        ide=body["ident"]
    )
    return {"token": token}  
  
  
#http://localhost:5000/fila/chamarNormal
@router.post("/fila/chamarNormal" ,
     summary="Chamar na fila sem prioridades  (Utiliza autenticação)",
    description="Chama quem está na fila em sua ordem de chegada sem respeitar prioridade 1 ou demais  ",
)
def chamar_normal(user=Depends(auth_token)):
    if(not user):
    	return "Erro de autenticação"
    try:
        pos = minhaFila.chamar_normal()
        return {"message": pos}
    except IndexError:
        raise HTTPException(status_code=404, detail="Fila vazia")

 
#http://localhost:5000/fila/chamarPrioridade
@router.post("/fila/chamarPrioridade",
     summary="Chamar na fila com prioridades  (Utiliza autenticação)",
    description="Chama quem está na fila respeitando a prioridade naqual 1 é a primeira , 2 é a segumda e 3 a ultima",
)
def chamar_prioridade(user=Depends(auth_token)):
    if( not user ):
        return "Erro de autenticação"
    try:
        pos = minhaFila.chamar_prioridade()
        return {"message" : pos }
    except IndexError :
        raise HTTPException(status_code=404, detail="Fila vazia")
 

 

 



