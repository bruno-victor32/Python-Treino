#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas minusculas
#Quantas letras aotodo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() #Estou retirando os espaços antes e depois
print('Analisando seu nome ')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Explicação da penultimo comando
#len(nome): A função len() retorna o número total de caracteres na string, incluindo espaços.

#nome.count(' '): O método count(' ') conta quantos espaços em branco existem na string nome.

#len(nome) - nome.count(' '): A subtração remove os espaços da contagem total de caracteres. Ou seja, ele conta quantas letras existem no nome, excluindo os espaços.

#Por exemplo, se o nome for "João Silva", a função len(nome) retornará 11 (que é o total de caracteres, incluindo o espaço). O nome.count(' ') contará 1 espaço. Então, a expressão 11 - 1 resultará em 10, ou seja, o nome tem 10 letras (sem contar o espaço).