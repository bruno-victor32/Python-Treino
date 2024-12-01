#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas minusculas
#Quantas letras aotodo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo '))

#Estou retirando os espaços do nome
nome_sem_espaco = nome.replace(' ','')

# Usa o split para dividir a string em palavras (por padrão, divide por espaços)
lista = nome.split()

print('O nome maiusculo é: {}'.format(nome.upper()))
print('O nome minusculo é: {}'.format(nome.lower()))
print('O total de letras, sem contar o espaço é {}'.format(len(nome_sem_espaco)))
print('O primeiro nome tem {} letras'.format(len(lista[0])))# Pega o primeiro elemento da lista e contar as letras