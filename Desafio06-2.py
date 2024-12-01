#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

# A função pow(),é uma função embutida em Python não sendo necessário importar nenhuma biblioteca.
# A função pow() em Python tem a finalidade principal de calcular potências.
# O primeiro argumento é o número que você quer elevar (neste caso, num),
# O segundo argumento é o expoente. Como a raiz quadrada de um número é o mesmo que elevar esse número à potência de 0,5 (ou 1/2), você passa 0.5 como segundo argumento.
# O f antes da string permite que você insira variáveis diretamente nas chaves {}


num = int(input('Digite um número: '))
raiz_quadrada = pow(num, 0.5)
num_dobro = (num * 2)
num_triplo = (num * 3)
print(f'O dobro de {num} é {num_dobro}')
print(f'O triplo de {num} é {num_triplo}')
print(f'A raiz quadrada de {num} é {raiz_quadrada:.3f}.')


