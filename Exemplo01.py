#Calcular a raiz quadrada de um número e arredondar para baixo

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num) #O sqrt permite calcular a raiz quadrada
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) #floor permite fazer o arredondamento para baixo