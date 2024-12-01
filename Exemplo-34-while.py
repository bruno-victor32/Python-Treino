#Imaginemos a situação na qual se deseja calcular e exibir a soma dos 10 primeiros números inteiros

soma = 0
termo = 1
while termo <= 10:
    soma = soma + termo #soma += termo
    termo = termo + 1 #termo += 1  #geração do termo da PA, de razão 1
print(soma)