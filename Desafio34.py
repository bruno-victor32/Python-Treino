#Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o valor do salário? '))
if salario > 1250:
    aumento = salario * 0.10
    total = aumento + salario
else:
    aumento = salario * 0.15
    total = aumento + salario
print(f'O valor do aumento é R${aumento:.2f} e do salario com o aumento será R${total:.2f}')