#Crie um programa que leia uma frase qualquer e diga se ela é um palindroma, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, - 1, -1): #segundo valor é aonde a contagem para, o terceiro valor indica que a sequência será gerada de forma decrescente
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo')

print('-=-' * 10)