#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o nome: '))
validacao = 'silva' in nome.lower()
print(f'Verificando o nome {nome} digitado se tem "SILVA"...')
print(f'Se a resposta for "True", significa que o nome "Silva" está presente no nome digitado: {validacao}')

#A função lower()
#convertetodo o nome para minúsculas, garantindo que a busca por "silva" seja feita de forma insensível a
# #maiúsculas/minúsculas. Isso significa que "Silva", "silva", "SILVA" etc., todos serão reconhecidos como "silva".