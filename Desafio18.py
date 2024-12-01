#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

grau = int(input('Digite o angulo do grau'))
grau_radiano = math.radians(grau) #Convertendo graus em radiano
seno = math.sin(grau_radiano)
cosseno = math.cos(grau_radiano)
tangente = math.tan(grau_radiano)
print(f'O valor do seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f} do angulo {grau}')