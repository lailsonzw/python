#META: Crie um progama que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiusculas;
#- quantas letras ao todo (sem considerar espaços);
#- quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
print('Nome com todas as letras maiusculas: {}'.format(nome.upper()))
print('Nome com todas as letras minusculas: {}'.format(nome.lower()))
print('Quantidade de letras do nome completo: {}'.format(len(nome.replace(' ',''))))
print('Quantidade de letras do primeiro nome: {}'.format(nome.find(' ')))
