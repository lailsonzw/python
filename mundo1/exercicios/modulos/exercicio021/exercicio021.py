#META: faça um progama em python que abra e reproduza o áudio de um arquivo MP3;

import playsound

playsound.playsound('/home/lailson/Desktop/Github/repositories/python/exercicioscurso/exercicio021/audiopy.ogg')
playsound.playsound('/home/lailson/Desktop/Github/repositories/python/exercicioscurso/exercicio021/motivação.mp3')

#Outro metodo

#import pygame

#pygame.init()
#pygame.mixer.music.load('motivação.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()