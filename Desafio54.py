#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
#ainda não atingiram a maioridade e quantas já são maiores

import datetime

ano_sistema = datetime.date.today().year

print('Programa que realiza a leitura de nascimento')
contador = 0
maior_idade = 0
menor_idade = 0
for cont in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if (ano_sistema) - ano < 18:
        menor_idade = menor_idade + 1
    else:
        maior_idade = maior_idade + 1
print(f'Foi digitado sete datas de nascimento. {maior_idade} pessoas são maiores de idade e {menor_idade} são menores de idade.')