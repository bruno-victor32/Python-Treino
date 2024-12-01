#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome da cidade: ')).strip()
cidade_maiuscula = cidade.upper()
lista = cidade_maiuscula.split()

validacao = 'SANTO' in lista[0]

print(f'O  nome da cidade digitado foi {cidade}')
print(validacao)