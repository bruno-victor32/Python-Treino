#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um número: '))

unidade = num % 10
dezena = ((num - unidade) // 10) % 10 #O operador // é importante para garantir que a divisão seja inteira (sem casas decimais)
centena = ((num - dezena) // 100) % 10
milhar = (num - centena) // 1000

print(f' A unidade é: {unidade}')
print(f' A dezena é: {dezena} ')
print(f'A centena é: {centena}')
print(f'A milhar é: {milhar}')