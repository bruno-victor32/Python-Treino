#Escreva um programa que leia dos números inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print(f'O primeiro valor {num1} é maior que o segundo valor {num2}')
elif num2 > num1:
    print(f'O  segundo valor {num2} é maior que o primeiro valor {num1}')
else:
    print('Não existe valor maior, os dois são iguais.')
