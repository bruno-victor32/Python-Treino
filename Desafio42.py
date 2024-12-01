#Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('-=-' * 20)
print('Verificando se é possível formar um triângulo')
print('-=-' * 20)
raio1 = int(input('Digite o comprimento da 1° reta: '))
raio2 = int(input('Digite o comprimento da 2° reta: '))
raio3 = int(input('Digite o comprimento da 3° reta: '))
if (raio1 + raio2) > raio3 and (raio1 + raio3) > raio2 and (raio2 + raio3) > raio1:
    print('É possível, podemos formar um triângulo!')
    if raio1 != raio2 and raio2 != raio3 and raio3 != raio1:
        print('É possível formar um triângulo escaleno "todos os lados diferentes"')
    elif (raio1 == raio2) and (raio2 == raio3) and (raio3 == raio1):
        print('É possível formar um triângulo equilátero "todos os lados iguais"')
    else:
        print('É possível formar um triângulo Isosceles "dois lados iguais"')
else:
    print('Não é possível formar um triângulo!')



