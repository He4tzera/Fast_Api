import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic.main import BaseModel
from Api import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Inputs(BaseModel):
    cep: str

global cep

@app.post('/postcep')
def post_cep(inputs:Inputs,):
    cep = inputs.cep
    print(cep)
    return consulta(cep)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)