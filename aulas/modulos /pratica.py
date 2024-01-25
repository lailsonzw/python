#from math import sqrt
#from math import ceil
#importei as funções da blibioteca

import math;

#importei a blibioteca math para utilizar suas funçoes;

num = int(input('Digite algum numero: '))
raiz = math.sqrt(num)#usando uma função da blibioteca matematica math;
print('A raiz quadrada de {} é igual a {} '.format(num, math.ceil(raiz)))
#ceil arredonda um numero quebrado para um valor maior, ceil é uma função que pertence a blibioteca math;