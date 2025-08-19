project/
│── backend/ (FastAPI)
│   │── app/
│   │   ├── main.py
│   │   ├── api/          # rotas
│   │   ├── models/       # ORM
│   │   ├── services/     # regra de negócio
│   │   ├── schemas/      # Pydantic
│   │   └── core/         # config
│
│── frontend/ (Next.js)
│   │── pages/            # rotas UI
│   │── components/       # componentes React
│   │── services/         # chamadas à API (fetch/axios)
│   │── styles/
│   │── next.config.js



preciso primeiro criar nos diretorios os arquivos __init__.py para indicar que a pasta é um pacote python 

indicado dois underscores antes e depois

touch __init__.py
cd api && touch __init__.py && cd ..
cd core && touch __init__.py && cd ..
cd models && touch __init__.py && cd ..
cd schemas && touch __init__.py && cd ..
cd services && touch __init__.py && cd ..


apos o processo e criar a api certinha no diretorio backend iniciar o servidor

uvicorn app.main:app --reload --host 0.0.0.0 --port 5000
https://api.whatsapp.com/send?phone=5534992374909&text=Olá%2C%20tudo%20bem%3F


Meu nome é Samuel e fui informado pelo SINE sobre a vaga de Almoxarife (código 8528670) e no processo foi orientado a entrar em contato com você pelo WhatsApp para enviar meu currículo e, se possível, agendar uma entrevista. 

https://api.whatsapp.com/send?phone=
https://api.whatsapp.com/send?phone=XXXXXXXXXXX
https://api.whatsapp.com/send?phone=XXXXXXXXXXX
