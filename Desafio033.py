#Faça um programa que leia três números e mostre qual é o maior e igual e o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 == n2 and n2 == n3 and n3 == n1:
    print('Os três números são digitados')
    if n1 == n2 and n2 == n3:
        print('Os dois números digitados são iguais')
elif n1 > n2 and n2 > n3:
    print('O primeiro número digitado e o maior  e o terceorp número é o menor')
    if n3 > n2:
        print('O primeiro número digitado e o maior  e o segundo número é o menor')

