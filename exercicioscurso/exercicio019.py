#META: criar um progama que faça um sorteio dos alunos listados - Feito;

from random import choice
from os import system

primeiro_aluno = input('Digite o nome do primeiro aluno: ')
system('clear')
segundo_aluno = input('Digite o nome do segundo aluno: ')
system('clear')
terceiro_aluno = input('Digite o nome do terceiro aluno: ')
system('clear')
quarto_aluno = input('Digite o nome do quarto aluno: ')
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
system('clear')
print('O aluno sorteado foi a/o {}'.format(choice(lista)))
#estava dando erro porque eu queria botar todas as variaves dentro do choice.
#como eu resolvi o erro, coloquei as variaves dentro de uma variavel