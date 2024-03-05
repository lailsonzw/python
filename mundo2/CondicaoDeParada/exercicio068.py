from random import *

vitoria = 0
while True:
    
    print('Par ou Impar')
    numero = int(input('Digite algum número: '))
    ParOuImpar = str(input('Par ou impar [P/I]'))
    adversario = randint(1, 20)
    resultado = numero + adversario
    
    if ParOuImpar.upper() == "P" and resultado %2 == 0:
        print(f'voce ganhou, pois {ParOuImpar} + {adversario} = {resultado}')
        vitoria = vitoria + 1

    elif ParOuImpar.upper() == "I" and resultado %2 != 0: 
        print(f'voce ganhou, pois {numero} + {adversario} = {resultado}')
        vitoria = vitoria + 1
        
    else:
        print(f'Voce perdeu! você ganhou {vitoria} vezes.')
        break
    