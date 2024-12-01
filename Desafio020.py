#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista_alunos = [n1, n2, n3, n4]

# Embaralhar a lista
random.shuffle(lista_alunos)

#Pegando o primeiro aluno da lista embaralhada
escolhido = lista_alunos[0]
print(f'O aluno escolhido foi {escolhido}')

#Pegando o segundo aluno da lista embaralhada
escolhido = lista_alunos[1]
print(f'O aluno escolhido foi {escolhido}')

#Pegando o terceiro aluno da lista embaralhada
escolhido = lista_alunos[2]
print(f'O aluno escolhido foi {escolhido}')

#Pegando o segundo aluno da lista embaralhada
escolhido = lista_alunos[3]
print(f'O aluno escolhido foi {escolhido}')