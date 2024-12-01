# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Exibe a tabuada do número
print(f"Tabuada do {numero}:")
for i in range(0, 11):  # Loop de 0 a 10, vai iniciar no 0 até o 11. O 11 não será incluido na sequencia
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# for é uma estrutura de repetição em Python