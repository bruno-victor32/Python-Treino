#Calcular a raiz quadrada importando somente a funcionalidade de raiz quadrada

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num) #O sqrt permite calcular a raiz quadrada
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))