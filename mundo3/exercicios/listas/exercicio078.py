from os import system

numeros = []
ordem = 0

while ordem < 5:
    
    numeros.append(input(f'Digite o numero da posicao {ordem}: '))
    ordem += 1   

system('clear') 

print(f'Numeros Digitados: {numeros}')
print(f'O maior numero da lista foi {max(numeros)} e sua posicao na lista é {numeros.index(max(numeros))}')
print(f'O menor numero da lista foi {min(numeros)} e sua posicao na lista é {numeros.index(min(numeros))}')
