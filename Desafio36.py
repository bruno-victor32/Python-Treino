#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal.
#Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('-=-' * 20)
print('Empréstimo Bancário')
print('-=-' * 20)
vl_casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o valor liquido do salário R$: '))
anos = int(input('Digite em quantos ano será pago a casa: '))
print('Calculando o valor da prestação mensal')
porc_sal = (salario * 30) / 100 # 30% do salario do funcionario
prestacao_mensal = vl_casa / (anos * 12)
if prestacao_mensal > porc_sal:
    print('Não será possível realizar o empréstimo!Emprestimo negado')
    print(f'O valor da prestação seria R${prestacao_mensal:.2f}')

else:
    print('Emprestimo autorizado')
    print(f'O valor da prestação vai ser R${prestacao_mensal:.2f}')
print(porc_sal)
