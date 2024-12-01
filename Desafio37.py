#Escreva um programa que leia um número inteiro qualquer e peça para
# o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('-=-' * 20)
print('Programa de conversão')
print('-=-' * 20)
num = int(input('Digite um número: '))
print('Digite "1" para conversão de inteiro para binário')
print('Digite "2" para conversão de inteiro para octal')
print('Digite "3" para conversão de inteiro para hexadecimal')
digito = int(input('Digite a opção desejada: '))
if digito == 1:
    binario = bin(num)
    print(f'O valor {num} digitado em binário é {binario} ')
elif digito == 2:
    octal = oct(num)
    print(f'O valor {num} digitado em octal é {octal} ')
else:
    hexadecimal = hex(num)
    print(f'O valor {num} digitado em hexadecimal é {hexadecimal} ')
