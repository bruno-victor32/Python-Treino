frase = 'Curso em Video de Python'

#Dividindo a string "frase" em uma lista de palavras e
palavras = frase.split()

# Juntando as palavras com o hífen ('-') como separador
resultado = '-'.join(palavras)

separando_strings = '-'.join(frase)
separando_com_espaços = ' '.join(frase)

print(palavras)
print(resultado)
print('----------')
print(separando_strings)
print(separando_com_espaços)