#Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu
# IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso atual KG: '))
altura = float(input('Digite a sua altura em Metros: '))

imc = peso / (altura ** 2)
print(f'A altura digitada {altura} metros e o peso {peso:.1f} Kg é o IMC calculado foi {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do Peso, seu IMC está abaixo de "18.5"')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal, seu IMC está entre 18.5 e 25')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso, seu IMC está entre 25 e 30')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade, seu IMC está entre 30 e 40')
else:
    print('Você está com obesidade mórbida, seu IMC está acima de 40')
