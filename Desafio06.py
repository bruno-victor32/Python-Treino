#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

import math     #Importando o módulo math

num = int(input('Digite  um valor: '))
raiz_quadrada = math.sqrt(num)
print('O valor digitado foi {}, \no dobro do número digitado é {},\no triplo do número digitado é {}\ne a raiz quadrada {:.3f}'.format(num, (num * 2), (num * 3), raiz_quadrada))

#Observações:

# {:.3f} - Estou formatando um número de ponto flutuante, ou seja, quero somente três casas virtuais depois da vírgula
# \n     - Permite quebrar linha
# sqrt() - A função sqrt() calcula a raiz quadrada do número fornecido