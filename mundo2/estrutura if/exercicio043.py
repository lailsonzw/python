#META: faça um progama que calcule o imc;
import math

sexo = str(input('digite seu sexo\nsexo: '))
peso = float(input('digite seu peso\npeso: '))
altura = float(input('digite sua altura\naltura: '))

imc = peso / math.pow(altura,2)

if imc <= 18.5:
    print('seu imc: {}, \033[1;31;40mvoce está abaixo do peso.'.format(imc))
elif imc <= 24.9:
    print('seu imc: {}, \033[1;32;40mvoce está no peso ideal.'.format(imc))
elif imc <= 29.9:
    print('seu imc: {}, \033[1;33;40mvoce está levimente acima do peso.'.format(imc))
elif imc <= 34.9:
    print('seu imc: {}, \033[1;31;40mvoce está com obesidade grau 1.'.format(imc))
elif imc <= 39.9:
    print('seu imc: {}, \033[1;31;40mvoce está com obesidade grau 2.'.format(imc))
elif imc > 40:
    print('seu imc: {}, \033[1;31;40mvoce está com obesidade grau 3(cuide disso antes que seja tarde).'.format(imc))



