print('\033[4;30;45m Olá, Mundo!\033[m')

print('\033[30m Olá, Mundo!\033[m')

print('\033[7;30m Olá, Mundo!\033[m')

print('\033[0;33;44m Olá, Mundo!\033[m')

print('\033[7;33;44m Olá, Mundo!\033[m')

nome = 'Guanabara'
print('Olá!Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

nome = 'Bruno'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))