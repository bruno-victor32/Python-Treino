#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade,
# se ele ainda vai se alistar ao serviço militar, se a hora de se alistar ou seja passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))