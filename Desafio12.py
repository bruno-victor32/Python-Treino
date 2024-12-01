#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor = float(input('Digite o valor da compra R$: '))
desc = int(input('Qual será o valor do desconto aplicado: '))
valor_desc = (desc / 100) * valor
valor_final = valor - valor_desc
print(f'O valor do produto é R${valor:.2f} e vai ter {desc}% de desconto')
print(f'O desconto será de R${valor_desc:.2f} portanto o valor final será R${valor_final:.2f}')
