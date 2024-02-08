#META: criar um progama que some todos o numeros multiplos de 3 impares de 1 ate 500;
soma = 0
cont = 0

for c in range(1, 501,2):
    if c%3 == 0:
        soma += c 
        cont += 1
        print(c, end=' ')
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))