#Faça um progama que leia pelo teclado um valor e mostre todos os dados posives dele;

algo = input("Digite algo ")
print('Seu tipo primitivo: {}'.format(type(algo)))
print(algo,'Possui apenas números?', algo.isnumeric())
print(algo,'Possui apenas letras?', algo.isalpha())
print(algo,'Possui letras ou números?', algo.isalnum())
print(algo,'Possui números de 0 a 9?', algo.isdecimal())
print(algo,'Possui todos as palavras em minúsculo?', algo.islower())
print(algo,'Possui espaços apenas espaços em branco?', algo.isspace())
print(algo,'Possui apenas letras maiúsculas?', algo.isupper())
print(algo,'Possui a primeira palavra maiúscula e o restante minúsculas?',algo.istitle())

#o que aprendi nesta aula:
# um novo jeito de mostrar o valor da variavel no print, como ver o tipo da variavel, vomo verificar oque tem dentro da variavel, como mudar o tipo da variavel no input;