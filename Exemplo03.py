#Calcular a raiz quadrada importando somente a funcionalidade de raiz quadrada e arredondando para baixo

#O sqrt permite calcular a raiz quadrada
#floor permite fazer o arredondamento para baixo

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))