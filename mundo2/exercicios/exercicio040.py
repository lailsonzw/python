#META: crie um progama que receba as notas de um aluno e depois calcule sua media e mostre se ele foi aprovado ou vai fazer recuperação ou reprovou

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))

media = (n1 + n2 + n3)/3

if media > 7.0:
    print('Este aluno fez media: {}, logo sua situação atual é \033[1;32;40mAPROVADO\033[0;0;0m'.format(media))
elif media > 5.0 and media < 6.9:
    print('Este aluno fez media: {}, logo sua situação atual é \033[1;33;40mRECUPERAÇÃO\033[0;0;0m'.format(media))
elif media < 5.0:
    print('Este aluno fez media: {}, logo sua situação atual é \033[1;31;40mREPROVADO\033[0;0;0m'.format(media))
