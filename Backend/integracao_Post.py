import uvicorn as uvicorn
from fastapi import FastAPI
from integracao import *
import json

global cep_usu


def cep_usu():
    cep = '04455310'
    return cep


app = FastAPI()


@app.post('/postcep')
async def post_cep():
    return cep_usu()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777, )
