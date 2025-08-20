👋 Olá , eu sou o Samuel Souto dos Santos / @sassa-afk 👀 ..

Tenho interesse na área de desenvolvimento de software 🌱
Atualmente estudo e crio projetos com intenção aplicar meus conhecimentos passados ao longo de minha experiência academica e no mercado de trabalho
📫 Você consegue chegar até mim através do email samuelsouto21@gmail.com .

# API REST de fila

Este projeto é uma API REST para gerenciamento de filas de atendimento. Permite adicionar clientes, consultar posição, chamar senhas em ordem ou por prioridade, além de proteger rotas sensíveis com autenticação JWT.

**OBS:** Neste primeiro momento, o foco está na estruturação do backend e na construção das APIs REST. O desenvolvimento da interface frontend será realizado em seguida, integrando com os serviços já preparados.

## Tecnologias

. Pythom fastApi . Python Jose (JWT) 

## Estrutura

O projeto está organizado em camadas seguindo uma estrutura DDD em Python puro com foco em APIs REST:

- project/: Raiz do repositório.
- project/backend/: Código do backend.
- project/backend/app/: App FastAPI (configuração e bootstrap).
- project/backend/app/main.py: Ponto de entrada da API (cria FastAPI, registra routers e deps).
- project/backend/app/api/: Camada de roteamento (endpoints).
- project/backend/app/api/GET/: Rotas GET (consultas: tamanho da fila, ver fila, posição).
- project/backend/app/api/POST/: Rotas POST (ações: entrar na fila, chamar normal/prioridade, gerar token).
- project/backend/app/core/: Núcleo de infra (segurança/JWT, configs).
- project/backend/app/services/: Regras de negócio.
- project/backend/app/models/: Modelos de domínio (entidades).
- project/backend/app/schemas/: Schemas Pydantic (request/response da API).

---
	|
	├── project
	│   ├── backend
	│   │   └── app
	│   │       │
	│   │       ├── api
	│   │       │   ├── GET   
	│   │       │   └── POST
	│   │       │
	│   │       ├── core
	│   │       │   
	│   │       ├── services
	│   │       │
	│   │       ├── models
	│   │       │
	│   │       ├── schemas
	│   │       │   
	│   │       └── services
	│   │
	    └── main.py
    
---

## Logica aplicada 

O main.py (project/main.py) é o ponto de entrada da aplicação, responsável por conectar todas as rotas definidas nas pastas GET e POST (project/backend/app/api/GET ou POST). Cada pasta contém o arquivo root.py, onde estão declaradas as rotas da API para leitura e escrita, respectivamente. Para autenticação e proteção das rotas sensíveis, os arquivos utilizam os serviços do security.py (project/backend/core/security.py), que gerencia a autenticação via JWT.

A pasta services/ contém a lógica de negócio da fila (project/backend/app/services/fila.py), como adicionar, remover e chamar clientes considerando prioridades. A pasta schemas/ define os modelos de dados para requisições e respostas, garantindo validação. A pasta models/ organiza os objetos que representam os dados do sistema, facilitando futura integração com banco de dados.

O arquivo main.py também escuta as rotas, gerencia segurança (JWT) e integra os serviços de modelagem de filas, instanciando funções nas rotas para realizar os processos de adição, visualização e remoção de clientes na fila.

Os arquivos de destaque estão em:

- project/main.py
- project/backend/app/api/GET/root.py
- project/backend/app/api/POST/root.py
- project/backend/app/core/security.py
- project/backend/app/services/fila.py


## Configuração do Ambiente (Linux)

Instalação : 

---
	python3 -m venv venv

	source venv/bin/activate

	pip install --upgrade pip

	pip install fastapi

	pip install "uvicorn[standard]"

	pip install python-jose[cryptography]
---

Para startar sua api execute : uvicorn app.main:app --reload --host 0.0.0.0 --port 5000

## Configuração do Ambiente (Virtual Render)
 
Primeiro suba seu projeto no github para sincronizar com o render em seguida, crue uma novo Web Service e conecte ao GitHub e escolha o repositório. Configure: 

---
	Environment: Python 3

	Build Command:

	pip install -r requirements.txt

 	Start Command:

	uvicorn main:app --host 0.0.0.0 --port 10000
---

OBS : Até o momento não havera varaiveis de ambientes configuradas no render

## Banco de Dados 

Até o momento, este projeto não possui integração com banco de dados. No entanto, essa funcionalidade será adicionada em versões futuras, acompanhando a evolução do sistema e possibilitando o armazenamento persistente das filas e usuários.

## Rotas criadas até o momento

**Rotas GET/POST**
 
| Método   | Rota                    | Descrição                                    |
| -------- | ----------------------- | -------------------------------------------- |
| **POST** | `/usuarios/`            | Cria um novo usuário na fila                 |
| **GET**  | `/usuarios/`            | Lista todos os usuários cadastrados          |
| **POST** | `/fila/entrar`          | Usuário entra na fila                        |
| **POST** | `/fila/sair/{id}`       | Remove um usuário da fila pelo ID            |
| **GET**  | `/fila/`                | Lista todos os usuários na fila em ordem     |
| **GET**  | `/fila/proximo`         | Retorna o próximo usuário a ser atendido     |
| **POST** | `/fila/prioridade/{id}` | Define prioridade para um usuário específico |
| **GET**  | `/fila/prioridade`      | Lista usuários em ordem de prioridade        |


## Documentação acessivel

A documentação das rotas criadas estão disponiveis nos links : 

- https://fila-l6vh.onrender.com/docs
- https://fila-l6vh.onrender.com/redoc
  







