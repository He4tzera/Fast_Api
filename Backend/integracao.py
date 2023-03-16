import uvicorn as uvicorn
from fastapi import FastAPI
from Api import *
from integracao_Post import *
import json

app = FastAPI()

@app.get('/getdata')
async def get_data():
    return consulta()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=7000)
