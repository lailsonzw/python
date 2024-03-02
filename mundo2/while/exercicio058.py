#META: melhorar o exercicio 028, agora o usuario vai tentar ate acerta, quando ele acertar mostre a quantidade de vezes que ele tentou


from os import *
from time import sleep
import random


quantidade = int(input('quantos numeros terão nessa rodada?\nnumeros: '))
erros = 0
print('Tente adivinhar o numero que o computador pensou entre 0 e {}\n'.format(quantidade))

numeroDigitado = int(input('Digite um numero: '))
numeroPensado = random.randint(0,quantidade)

print('verificando...')
sleep(2)
system('clear')

if numeroDigitado == numeroPensado:
    print('NOSSA! você acertou de primeira')
else:
    while numeroDigitado != numeroPensado:
        numeroDigitado = int(input('Não foi esse o numero que o computador pensou, tente novamente: '))
        erros += 1

print('Parabens você acertou!!! foi preciso de {} tentativas para acertar. O número sorteado foi {}'.format(erros,numeroPensado))
