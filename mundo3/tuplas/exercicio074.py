from random import randint
from os import system

numeros = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
        
system('clear')
print(numeros)
print(f'Menor numero: {max(numeros)}')
print(f'Maior numero: {min(numeros)}')

