#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import floor  #Importando somente a funcionalidade floor que permite fazer o arredondamento para baixo

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, floor(num)))



