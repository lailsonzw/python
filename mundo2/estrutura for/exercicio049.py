#META: criar um progama que o usario escolha um numero para fazer a taboada;

numero = int(input('Digite um numero para o progama gerar a taboada: '))

print('Taboada do {}'.format(numero))
for ordem in range(1,11,1):
    print('{} x {} = {}'.format(numero, ordem, numero * ordem))
    