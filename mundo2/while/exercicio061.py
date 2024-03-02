#META: faça a mesma coisa do exercicio 51, mas usando while

primeirotermo = int(input('primeiro termo: '))
razao = int(input('razao: '))
termo = primeirotermo
cont = 1

while cont <= 10:

    print('{} -> '.format(termo), end= ' ')
    termo += razao
    cont += 1
    
print('ACABOU')