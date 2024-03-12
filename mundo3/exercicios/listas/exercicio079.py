from os import system

numeros = list()
while True: 
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('valor duplicado! não vooou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

system('clear')    

print('=' * 30)
print(f'Ordem normal: {numeros}')
print(f'Ordem crescente: {sorted(numeros)}')
print('=' * 30)
