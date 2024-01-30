#META: crie um codigo que leia um numero de 0 a 9999 e mostre na tela cada digito separado;


print('SEPARADOR DE NUMEROS')
Numero = int(input('Digite um numero: '))
print('\n')

unidade = Numero // 1 % 10
dezena = Numero // 10 % 10
centena = Numero // 100 % 10
milhar = Numero // 1000 % 10


print('Numero digitado:\n'.format(Numero))
print('Unidade: {}\n'.format(round(unidade)))
print('Dezena: {}\n'.format(round(dezena)))
print('Centena: {}\n'.format(round(centena)))
print('Milhar: {}\n'.format(round(milhar)))



