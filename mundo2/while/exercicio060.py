#META: faça um progamaque leia um número qualquer e mostre o seu fatorial. Ex: 5 = 5*4*3*2*1 = 120

numero = int(input('Digite qualquer número para calcular seu fatorial: '))
fatorial = 1
NumBase = numero

while NumBase > 0: 
    
    fatorial *= NumBase
    NumBase -= 1

print('O fatorial de {} é {}'.format(numero,fatorial))    