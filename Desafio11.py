#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessaria para pintá-la
#Sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
quant_tinta = area / 2
print(f'A área é {area}m² é a quantidade tinta necessário para pintar é {quant_tinta} litros de tinta')