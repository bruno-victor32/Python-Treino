

import pyautogui

import time

pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5

#Abrir o google drive no meu computador, através do navegador EDGE
pyautogui.press('winleft')
pyautogui.write('Edge')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/u/0/home')
pyautogui.press('enter')
pyautogui.hotkey('shift', 'winleft')

#Entrar na minha área de Trabalho
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1866, 44)
pyautogui.mouseDown()
pyautogui.moveTo(1094, 769) #x, y - mouse

#Enquanto eu estou arrastando, vou mudar para o google drive
pyautogui.hotkey('alt', 'tab')
time.sleep(3)

#larguei o arquivo no google drive
pyautogui.mouseUp()
#Esperar 5 segundos
time.sleep(5)

pyautogui.alert("O código acabou a tarefa, por favor utilizar normalmente o computador. Obrigado!")

#nome = pyautogui.position()
#print(nome)