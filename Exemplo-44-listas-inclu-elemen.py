# incluindo elementos em uma determinada lista utilizando o método append()

atrizes = ['Paolla de Oliveira']
atrizes.append('Camila Queiroz')
while True:
    nome = input('Digite o nome de uma atriz: ')
    atrizes.append(nome)
    resp = input('Deseja continuar [S][N]? ')
    if resp.upper() == 'N':
        break
print(atrizes)