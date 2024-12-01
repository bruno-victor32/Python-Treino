#Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido

import random

lista_alunos = ["Matheus", "Bruno", "Alex", "Fernando"]
alunos_sorteado = random.choice(lista_alunos)
print(f'O nome do aluno sorteador foi "{alunos_sorteado}"')