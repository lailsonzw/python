#fazer um alarme em python

import playsound
from time import sleep
import os

contagem = int(input('quanto tempo será a contagem?\ntempo: '))
tempo = contagem

som = int(input('escolha um som\n1 iphone\n2 bom dia fazendia\nEscolha: '))

for c in range(contagem,-1,-1):
    
    print('TEMPO RESTANTE: {}'.format(tempo))
    sleep(1)
    tempo = tempo -1

if som == 1:
    playsound.playsound('/home/lailson/Desktop/Github/repositories/python/projetos/alarme/dsp.mp3')
elif som == 2:
    playsound.playsound('/home/lailson/Desktop/Github/repositories/python/projetos/alarme/dsp2.mp3')
else:
    print('Nao foi possivel encontrar o som.')