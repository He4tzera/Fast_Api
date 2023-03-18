import requests
import json
from integracao import *

def consulta():
    global dados_Logradouro, dados_Bairro, dados_Localidade
    try:
        #url para consulta do Cep
        url_Api = f'https://viacep.com.br/ws/{cep_usu()}/json/'
        print(cep_usu())
        requisicao = requests.get(url_Api)
        dados_Json = requisicao.content
        dados = json.loads(dados_Json)

        dados_Logradouro = dados['logradouro']
        dados_Bairro = dados["bairro"]
        dados_Localidade = dados['localidade']
        return dados_Logradouro, dados_Bairro, dados_Localidade
    #Except para caso o usuario insira um cep invalido
    except:
        print("Informe um CEP valido")
        return "Informe um CEP valido"
