#META: faça um radar que multe o usuario caso ele pase do limite;

print('se a velocidade passar de 100 km voce serar multado com um valor fixo de 100$ + 5%  por cada km a mais')
velocidade = float(input('qual a velocidade atual do carro: '))
multa = velocidade + ((5/100) * 100)                                                                                                                                                                                                                                                                                                                                                                 

if velocidade > 100:
    print('Voce ultrapassou o limite develocidade e será multado\n valor da muta: {}'.format(multa))