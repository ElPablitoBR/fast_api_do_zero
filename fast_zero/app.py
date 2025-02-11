from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá mundo!'}


# Servindo o diretório htmlcov como arquivos estáticos
app.mount(
    '/report',
    StaticFiles(directory='htmlcov', html=True),
    name='report',
)
