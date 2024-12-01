#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
frase_minuscula = frase.lower()
letra_a = frase_minuscula.count('a')
posicao_inicial = frase_minuscula.find('a')
posicao_final = frase_minuscula[::-1].find('a')
print(f'A letra "a" aparece {letra_a} vezes na frase')
print(f'A letra "a" aparece a primeira vez na posição {posicao_inicial}')
print(f'A letra "a" aparece a última vez na posição {posicao_final}')
