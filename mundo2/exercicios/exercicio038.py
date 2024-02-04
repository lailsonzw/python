#META: faca um progama que compare dois valores e depois motre o maior ou mostre se são iguais;

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 > v2:
    print('O valor {} é o maior numero'.format(v1))
elif v2 > v1: 
    print('O valor {} é o maior numero'.format(v2))
else:
    print('Os valores possuem o mesmo tamanho.')
