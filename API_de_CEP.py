#Consulta de informações de um CEP

import requests

cep = str(input('Digite o CEP (8 Dígitos)'))

cep = cep.replace("-","").replace(".","").replace(" ","")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao)
    print(requisicao.json())

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(f'A cidade é {cidade} - {uf}, o bairro {bairro}.')
else:
    print('CEP Inválido')

#Observação:
# Código 200 significa que deu certo a requisição
# Código 400 significa que não deu certo a requisição


