#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até
#200km e R$0,45 para viagens mais longas

distancia = int(input('Digite a distância em KM do inicio da viagem até o final:'))
if distancia <= 200:
    preco_passagem = distancia * 0.50
    print(f'O preço da passagem será R${preco_passagem:.2f}')
else:
    preco_passagem = distancia * 0.45
    print(f'O preço da passagem será R${preco_passagem:.2f}')
