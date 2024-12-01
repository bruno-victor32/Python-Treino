#A confederação nacional de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade
# Até 9 anos: MIRIM         Até 19 anos: JUNIOR
# Ate 14 anos: INFANTIL     Até 25 anos: SÊNIOR
# Acima: MASTER

import datetime

print('-=-' * 20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-' * 20)
nasc = int(input('Digite a sua data de nascimento: '))
ano_atual = datetime.date.today() #Data do sistema
idade = ano_atual.year - nasc #Ano Atual - ano de nascimento
print(f'A idade atual do atleta é {idade}')
if idade <= 9:
    print('Atleta faz parte da categoria "MIRIM"')
elif idade > 9 and idade <= 14:
    print('Atleta faz parte da categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Atleta faz parte da categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Atleta faz parte da categoria SÊNIOR')
else:
    print('Atleta faz parte da categoria MASTER')