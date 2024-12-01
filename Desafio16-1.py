#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

#A função trunc() em Python é usada para truncar um número, ou seja, remover a parte decimal e manter apenas a parte inteira.
#A função trunc() não arredonda para baixo
import math

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'. format(num, math.trunc(num)))