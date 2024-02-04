#META: faça um progama para verificar se é possivel criar um triangulo e depois classifique o tipo desse triangulo

#META: crie um progama para verificar se é possivel criar um triangulo, leia os 3 segmentos;


seg1 = float(input('digite o tamanho do 1 segmento: '))
seg2 = float(input('digite o tamanho do 2 segmento: '))
seg3 = float(input('digite o tamanho do 3 segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg3 + seg2 > seg1:
    if seg1 == seg2 and seg3:
        print('É possivel criar um triangulo Equilátero, pois seus lados são iguais')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('É possivel formar um triangulo Isósceles, pois existem dois lados com tamanhos iguais')
    elif seg1 != seg2 or seg1 != seg3 or seg2 != seg3:
        print('É possivel formar um triangulo Escaleno, pois seus lados são diferentes')
else: 
    print("Não é possivel montar um triangulo")