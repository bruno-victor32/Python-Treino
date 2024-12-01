#Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo

print('-=-' * 20)
print('Verificando se é possível formar um triângulo')
print('-=-' * 20)
raio1 = int(input('Digite o comprimento da 1° reta: '))
raio2 = int(input('Digite o comprimento da 2° reta: '))
raio3 = int(input('Digite o comprimento da 3° reta: '))
if (raio1 + raio2) > raio3 and (raio1 + raio3) > raio2 and (raio2 + raio3) > raio1:
        print('É possível, podemos formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')