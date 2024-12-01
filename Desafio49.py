#Refaça o DESAFIO 009 ,mostrando a tabuada de um número que o usuário
#escolher, só que agora utilizando um laço for

print('-=-' * 20)
print('-=-=- TABUADA -=-=-')
print('-=-' * 20)
valor = int(input('Digite a tabuada desejada: '))

for contador in range(0, 11):
    tabuada = contador
    tabuada = tabuada * valor
    print(f'A tabuada do "{valor}" é {contador} x {valor} = {tabuada}')