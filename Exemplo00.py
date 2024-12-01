#Calcular a raiz quadrada de um número

import math   #Importando o módulo, biblioteca "math"
num = int(input('Digite um número: '))
raiz = math.sqrt(num)        #O sqrt permite calcular a raiz quadrada
print('A raiz de {} é igual a {}'.format(num, raiz))