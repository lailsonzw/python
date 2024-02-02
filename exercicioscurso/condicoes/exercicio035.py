#META: crie um progama para verificar se é possivel criar um triangulo, leia os 3 segmentos;


seg1 = float(input('digite o tamanho do 1 segmento: '))
seg2 = float(input('digite o tamanho do 2 segmento: '))
seg3 = float(input('digite o tamanho do 3 segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg3 + seg2 > seg1:
    print("É possivel montar um triangulo")
else: 
    print("Não é possivel montar um triangulo")