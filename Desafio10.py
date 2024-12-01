#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dólares ela pode comprar

saldo = float(input('Digite o valor que tem na conta em R$: '))
cotacao_dolar = float(input('Digite o valor da cotação do dólar atual: '))

#quantidade de dolares que posso comprar
quant_dolar = saldo / cotacao_dolar
print(f'Com a quantia R$ {saldo:.2f} posso comprar US$ {quant_dolar:.2f} dólares')
