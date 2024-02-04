#META: criar um codigo que verifique se o numero é impar ou par;


numero = int(input('Digite qualquer numero: \n'))

if numero % 2 == 0:
    print('{} é par'.format(numero))
else:
    print('{} é impar'.format(numero))