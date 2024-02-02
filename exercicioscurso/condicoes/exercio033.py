#META: faça um progama que receba 3 numeros e mostre o maior numero digitado e o menor numero;

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = int(input('digite o terceiro numero: '))

maiornumero = 0
menornumero = 0

if num1 > num2:
    maiornumero = num1
else:
    maiornumero = num2
if num3 > num2:
    maiornumero = num3

if num1 < num2:
    menornumero = num1
else:
    menornumero = num2
if num3 < num2:
    menornumero = num3
    
print('O maior numero digitado foi: {}'.format(maiornumero))
print('O menor numero digitado foi: {}'.format(menornumero))