#Crie um programa no qual o usuário informe um número
#inteiro positivo N e armazene-o em uma variável. Em seguida,
#o usuário deve digitar N números. Ao fim, o programa deve
# imprimir a média aritmética dos N números digitados.

cont = 0
soma = 0

while True:
    num = int(input('Digite um número (ou 0 para sair): '))

    # Se o usuário digitar 0, o loop será encerrado
    if num == 0:
        break

    soma += num  # Soma os números digitados
    cont += 1  # Conta quantos números foram digitados

# Verifica se algum número foi digitado
if cont > 0:
    media = soma / cont  # Calcula a média
    print(f'Média aritmética: {media:.2f}')
else:
    print('Não foi possível calcular a média, pois nenhum número válido foi inserido.')

print('Fim do Programa')
