#META crie um progama que leia um numero real e depois mostre sua parte inteira, exemplo: 6.9979, parte inteira = 6;
import math

numero = float(input('Digite qualquer numero: '))

print('Numero = {}, sua parte inteira = {}'.format(numero, math.trunc(numero)))