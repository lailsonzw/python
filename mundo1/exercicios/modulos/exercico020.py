#META: criar um progama que sorteie uma lista sem repitir nomes;

from random import shuffle

name1 = input('Digite o primeiro name:\n')
name2 = input('Digite o segundo name:\n')
name3 = input('Digite o terceiro name:\n')
name4 = input('Digite o quarto nome:\n')
list = [name1, name2, name3, name4]

shuffle(list)

print('A ordem de apresentação será\n')
print(list)