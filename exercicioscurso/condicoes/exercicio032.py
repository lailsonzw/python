#Faça um progama que mostre se o ano é bissexto;

ano = int(input('digite algum ano para verificar se ele é bissexto: \n'))

if ano % 4 == 0:
    print('{} é bissexto'.format(ano))
else: 
    print('{} não é bissexto'.format(ano))