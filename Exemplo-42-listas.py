#Lista vazia

idades = []

# Lista com elementos pré-definidos
idades = [27, 19, 33, 47]

# Cada um dos elementos da lista "dados" é de um tipo distinto
# Nome da atriz é uma string
# Quantidade de filhos é um inteiro
# Estatura é um valor real
# Informação relacionada ao uso do Instagram é um valor lógico

dados = ['Caroline Paola Oliveira da Silva', 0, 1.70, True]
print(dados)
print('\n')
print(f'Nome: {dados[0]}')
print(f'Quantidade de filhos: {dados[1]}')
print(f'Estatura: {dados[2]:.2f}m')
if dados[3] == True:
    print(f'Usa Instagram: Sim')
else:
    print(f'Usa Instagram: Não')
