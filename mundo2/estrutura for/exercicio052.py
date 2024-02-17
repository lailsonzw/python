#META: criar um progama para verificar se o numero é primo;

numero = int(input('digite algum numero para ser verificado: '))
contador = 0

for divisao in range(1,numero + 1):
    print('{} '.format(divisao),end='')
if contador > 2:
    print('\n\033[0mO numero {} não é primo.'.format(numero))
else:
    print('\n\033[0mO numero {} é primo.'.format(numero))