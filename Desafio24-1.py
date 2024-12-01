#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

#Explicação: selecionar os primeiros 5 caracteres que estão amarzenado na variavel "cidade",
#convertê-los para maiúsculas e compará-los com a string "SANTO",
#o resultado será True ou False.