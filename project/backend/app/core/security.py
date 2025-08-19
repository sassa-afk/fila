from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Optional  
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "chave_secreta"   
ALGORITMO = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 720

def new_token(dados: dict, ide: str, expire_delta: Optional[timedelta] = None):
    to_encode = dados.copy()
    expire = datetime.utcnow() + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN))
    to_encode.update({"exp": expire, "ide": ide})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITMO)
    
 
security = HTTPBearer()

def auth_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        return payload   # devolve os dados decodificados do token
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

