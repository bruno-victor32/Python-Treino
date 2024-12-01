# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
#artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

print('-=-' * 20)
print('Contagem regressiva de fogos de artificio')
print('-=-' * 20)
contador = 11
for c in range(10,-1, -1):
    print(c)
    time.sleep(1)
