#Faça um programa que calcule a soma entre todos os
#números impares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500


cont = 0
soma = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma = soma + contador
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))



