# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número inteiro: '))
print('-=-' * 20)
print('Verificando se é um número primo.')
print('-=-' * 20)
if num % 1 == 0 and num % num == 0:
    print('É um número primo')
else:
    print('Não é um número primo')