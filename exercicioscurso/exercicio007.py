#META: faça um progama que calcule a media do aluno utilizando variaves do tipo float;

primeiranota = float(input('Digite a primeira nota do aluno: '))
segundanota = float(input('Digite a segunda nota do aluno: '))

media = (primeiranota + segundanota)/2

print('A media final do aluno foi de {:.1} pontos'.format(media))