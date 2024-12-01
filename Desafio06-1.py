#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número:'))
print('Dobro do {} é {}'.format(num, (num * 2)))
print('Triplo do {} é {}'.format(num, (num * 3)))
print('Raiz quadrada do {} é {:.3f}'.format(num, (num ** 0.5)))
