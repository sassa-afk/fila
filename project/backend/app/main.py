from fastapi import FastAPI
from app.api.GET import root as get_root
from app.api.POST import root as post_root
from app.core import security as security
from app.services.Fila import Fila

 
 


app = FastAPI(
    title="API de Gerenciamento de Fila",
    version="1.0",
    description="""
    Visão Geral : 
    
    Esta API gerencia filas de atendimento com suporte a prioridades e autenticação via JWT para chamar em prioridades.

    ## Funcionalidades
    
    - Adicionar clientes na fila, com ou sem prioridade.
    - Consultar o tamanho atual da fila.
    - Verificar a posição de um cliente na fila usando a senha gerada.
    - Chamar clientes da fila, considerando a prioridade quando aplicável.
    - Proteção de rotas sensíveis usando autenticação JWT.

    ## Uso
    
    - Ideal para sistemas de atendimento, controle de senhas e filas de serviço, com foco em simplicidade e segurança.
    """,
    Portilio ="https://sassa-afk.github.io/pagina1/" 
    
 

)



minhaFila = Fila()

#  instancia da fila para os routers
get_root.set_fila(minhaFila) 
post_root.set_fila(minhaFila)

get_root.set_auth(security) 
post_root.set_auth(security)
 
 
# inclusao do app rotas no main
app.include_router(get_root.router)
app.include_router(post_root.router)

