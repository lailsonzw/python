#META: melhorar o desafio 61, perguntando ao usuario se ele quer mostrar mais alguns termos. O progama ancerra quando ele disser que quer mostrar os termos;

#META: faça a mesma coisa do exercicio 51, mas usando while

primeirotermo = int(input('primeiro termo: '))
razao = int(input('razao: '))
termo = primeirotermo
cont = 1
total= 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end= ' ')
        termo += razao
        cont += 1
    print('PAUSE')
    mais = int(input('quantos termos a mais voce irar adicionar? '))

print("progressão finalizada com {} termos mostrados.".format(total))
print('ACABOU')