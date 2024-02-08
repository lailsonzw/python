#META: Criar um jogo que o usuario adivinhe o numero, caso ele erre será dado dicas;
from random import randint
from os import system
import playsound

quantidade = int(input('Quantos numeros teremos?\nquantidade: '))
print("Digite um numero entre 1 e {}".format(quantidade))
numerodig = int(input('Numero: '))
numeropc = randint(1,quantidade)

while numeropc != numerodig:
    if numerodig > numeropc:
        print('Você digitou um numero maior que o do pc, DICA: digite um numero menor')
        numerodig = int(input('Numero: '))
        system('clear')
    elif numerodig < numeropc:
        print('Você digitou um numero menor que o do pc, DICA: digite um numero maior')
        numerodig = int(input('Numero: '))
        system('clear')

print("\033[1;32;40mPARABENS!! VOCE ACERTOU,\033[0;30;40mo numero que o computador escolheu foi: {}".format(numeropc)) 


