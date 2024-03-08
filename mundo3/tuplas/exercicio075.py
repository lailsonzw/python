from os import system


numeros = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
NumeorsPar = 0
ordem = 0

for ordem in numeros:
    if ordem % 2 == 0:
        NumeorsPar += 1

print(f'Você digitou os valores {numeros}')
print(f'O valor 5 apareceu {numeros.count(5)}')
print(f'O valor {numeros[2]} aparece na posicao {numeros.index(numeros[2])}')
print(f'Dentro dessa tupla exitem {NumeorsPar} numeros pares!')
test = input('Digite qualquer tecla')
system('clear')
print('PROGAMA ENCERRADO.')
