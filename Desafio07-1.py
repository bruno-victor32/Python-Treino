#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

# Modulo statistics, contém várias funções úteis para realizar operações estatísticas, incluindo o cálculo da média.
# Uma lista em Python é uma estrutura de dados que permite armazenar uma coleção de itens.
# Esses itens podem ser de qualquer tipo, como números, strings ou até outras listas.
import statistics

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
numero = [nota1, nota2]    #Definindo uma lista chamada numero
media = statistics.mean(numero)   #Calculo da média
print(f'A primeira nota foi {nota1}, a segunda nota foi {nota2} e a média foi {media} ')

