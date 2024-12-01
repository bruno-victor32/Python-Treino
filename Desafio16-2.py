#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#Para conseguir pegar somente o número inteiro digitado, no final converto de float para int o número digitado pelo usuário