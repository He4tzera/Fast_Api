import uvicorn as uvicorn
from fastapi import FastAPI
from Api import *
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
def cep_usu():
    cep = '04434240'
    return cep

origins = [
    "*"
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
@app.post('/postcep')
async def post_cep():
    return cep_usu()

@app.get('/getdata')
async def get_data():
    return consulta()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=7777)
