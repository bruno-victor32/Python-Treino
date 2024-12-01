#Faça um programa que leia o salario de um funcionario e mostre seu novo salario
# ,com15% de aumento.

salario = float(input('Digite o valor do salario R$: '))
aumento = int(input('Qual será o valor do aumento aplicado em porcentagem: '))
valor_aumento = (aumento / 100) * salario
valor_final = salario + valor_aumento
print(f'O valor do salário é R${salario:.2f} e vai ter {aumento}% de aumento')
print(f'O aumento será de R${valor_aumento:.2f} portanto o valor final será R${valor_final:.2f}')