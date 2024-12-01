#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade,
# se ele ainda vai se alistar ao serviço militar, se a hora de se alistar ou seja passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import datetime

print('-=-' * 20)
print('--- Alistamento Militar')
print('-=-' * 20)
nasc = int(input('Digite o ano de nascimento '))
ano_atual = datetime.date.today() #Data do sistema
idade = ano_atual.year - nasc #Ano Atual - ano de nascimento
print(f'Sua idade é {idade} anos')
if idade < 18:
    print('Não está na idade de se apresentar a junta militar')
    falta_anos = 18 - idade
    print(f'Falta {falta_anos} ano(s)')
elif idade == 18:
    print('Está no momento certo de se alistar ao exercito. Se apresente a junta militar')
else:
    print('Já passou  o tempo de alistamento')



