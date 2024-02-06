#META: faça um jogo do pedra,papel e tesoura
from os import *
from time import *
from random import *

print('escolha algum desses:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n')
escolha = int(input('Escolha: '))

computador = randint(0,2)
system('clear')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if escolha == 0 and computador == 0:
    print('Ops, aconteceu um empate o compultador tambem escolheu pedra...')
elif escolha == 0 and computador == 1:
    print('Papel engole pedra, infelizmente não foi dessa vez...')
elif escolha == 0 and computador == 2:
    print('Pedra quebra tesoura! parabens, você ganhou')
    
if escolha == 1 and computador == 0:
    print('papel engole pedra! parabens você ganhou!')
elif escolha == 1 and computador == 1:
    print('Ops, aconteceu um empate o compultador tambem escolheu papel...')
elif escolha == 1 and computador == 2:
    print('papel e cortado por tesoura, não foi dessa vez')

if escolha == 2 and computador == 0:
    print('tesoura e quebrada pela pedra, não foi dessa vez!')
elif escolha == 2 and computador == 1:
    print('tesoura corta papel! parabens você ganhou!')
elif escolha == 2 and computador == 2:
    print('Ops, aconteceu um empate o compultador tambem escolheu papel...')

else: 
    print('error, try again!')
