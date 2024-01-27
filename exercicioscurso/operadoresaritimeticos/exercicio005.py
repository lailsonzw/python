#Meta: fazer um progama que leia um numero e depois mostre seu sucessor e antecessor;

numero = int(input('Digite qualquer numero: '))

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(numero, (numero - 1), (numero + 1)))