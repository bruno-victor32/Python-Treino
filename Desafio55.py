#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lido.

maior_peso = 0
menor_peso = 500
for con in range(0,5):
    peso_digitado = float(input('Digite o seu peso KG: '))
    if peso_digitado > maior_peso:
        maior_peso = peso_digitado
    if peso_digitado < menor_peso:
        menor_peso = peso_digitado
print(f'0 maior peso digitado foi {maior_peso} e o menor foi {menor_peso}')

