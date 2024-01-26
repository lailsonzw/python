#META: criar um progama que leia um agulo qualquer e mostrar na tela o valor de seno, cosseno e a tangente desse angulo;
import math

angulo = float(input('Digite qualquer angulo que vinher em sua cabeça\nAgulo: '))
print('Angulo = {}, Seno = {:.2}, Cosseno {:.2}, Tangente {:.2}'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))