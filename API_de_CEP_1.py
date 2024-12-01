# BUSCA DE CEP A PARTIR DE ENDEREÇO

import requests
import pprint

uf = "RJ"
cidade = "Rio de Janeiro"
endereco = "Rio Branco"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
print(requisicao)

dic_requisicao = requisicao.json()
print(dic_requisicao)
pprint.pprint(dic_requisicao)