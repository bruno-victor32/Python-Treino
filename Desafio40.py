#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida
# - Media abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
print('-=-' * 20)
print('De acordo com a média atingida')
print('-=-' * 20)
if media < 5.0:
    print(f'A média {media:.1f} atingida ficou abaixo de "5.0" ')
    print('O aluno está REPROVADO')
elif (media >= 5) and (media <= 6.9):
    print(f'A média {media:.1f} atingida ficou entre "5" e "6.9" ')
    print('O aluno está de RECUPERAÇÃO')
elif media >= 7.0:
    print(f'A média {media:.1f} atingida ficou igual a 7 ou superior ')
    print('O aluno está APROVADO')