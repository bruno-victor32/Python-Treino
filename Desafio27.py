# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo
# nome separadamente
# Exemplo: Ana Maria de Souza
# Primeiro = Ana
# Ultimo = Souza

nome = str(input('Digite o nome completo: ')).strip()
lista = nome.split()
print('Primeiro nome digitado foi: {}'.format(lista[0])) #Estou utilizando o 0 para pegar o primeiro item/nome da lista
print('O último nome digitado foi: {}'.format(lista[-1])) #Estou utilizando o -1 para pegar o último item/nome da lista