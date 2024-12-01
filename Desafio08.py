#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
#milimetros

num = float(input('Digite um valor a ser convertido:'))
print('O valor digitado foi {}'.format(num))
print('O valor em "cm" é: {:.0f} cm '.format((num * 100)))
print('O valor em "mm" é: {:.0f} mm'.format((num * 1000)))