#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo de áudio
pygame.mixer.music.load('Acalma o Meu Coração   Anderson Freire.mp3')

# Reproduzir o áudio
pygame.mixer.music.play()

input('Agora você escuta?')