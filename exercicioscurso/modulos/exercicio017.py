#META: faça um programa que leia o comprimento do cateto aposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa;

#para fazer esse progama temos que saber como calcular o comprimento da hipotenusa;
#Formula para calcular a hipotenusa: H = Raiz quadrada da soma dos 1C² + 2C²;

#vamos adicionar variaves para guardar o comprimento do cateto oposto e o cateto adjacente;
from math import hypot

cateto_oposto = float(input('digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)#função da blibioteca math que calcula automaticamente a hipotenusa do triangulo

print('A hipotenusa vai medir {:.3}'.format(hipotenusa))

