#META: faça um jogo para o usuario tentar adivinhar o numero digitado pelo computador;
from os import *
from time import sleep
import random

print('Tente adivinhar o numero que o computador pensou entre 0 e 5\n')

numerodigitado = int(input('Digite um numero: '))
numeropensado = random.randint(0,5)

print('processando')

system('clear')

if numerodigitado == numeropensado:
    print('Parabens, voce acertou')
else:
    print('não foi dessa vez, o numero escolhido foi {}'.format(numeropensado))