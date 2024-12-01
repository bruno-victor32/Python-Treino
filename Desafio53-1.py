#Crie um programa que leia uma frase qualquer e diga se ela é um palindroma, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1] #Não especificamos inicio nem fim, então o fatiamento vai percorrer toda a string.O -1 no final significa que o passo será negativo, ou seja, a sequência será lida de trás para frente.
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo')