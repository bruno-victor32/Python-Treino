#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

import math

comprimento_cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
comprimento_cat_adjace = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(comprimento_cat_oposto ** 2 + comprimento_cat_adjace ** 2)

print(f'O valor do comprimento do cateto oposto é {comprimento_cat_oposto}, do cateto adjacente é {comprimento_cat_adjace} e da hipotenusa é {hipotenusa}')