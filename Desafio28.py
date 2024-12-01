#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
#deverá escrever na tela se o usuário venceu ou perdeu

import random

numero_digitado = int(input('Digite um número: '))
num = random.randint(0,5)
if numero_digitado == num:
    print(f'O número digitado é {numero_digitado} e o sorteado foi {num}. Parabéns, você acertou!!!')
else:
    print(f'O número digitado é {numero_digitado} e o sorteado foi {num}. Você errou, tente novamente!!!')

