#META: crie um progama que diga as categorias dos atletas: mirim, infantil, junior, senior, master;

idade = int(input('O atleta nasceu em qual ano?\nano: '))

verificacao = 2023 - idade

if verificacao < 10:
    print('O atleta nasceu em {} e tem {} anos, portanto sua categoria é mirim'.format(idade, verificacao))
elif verificacao < 15:
    print('O atleta nasceu em {} e tem {} anos, portanto sua categoria é infantil'.format(idade, verificacao))
elif verificacao < 20:
    print('O atleta nasceu em {} e tem {} anos, portanto sua categoria é junior'.format(idade, verificacao))
elif verificacao < 26:
    print('O atleta nasceu em {} e tem {} anos, portanto sua categoria é sênior'.format(idade, verificacao))
elif verificacao > 26:
    print('O atleta nasceu em {} e tem {} anos, portanto sua categoria é MASTER!!'.format(idade, verificacao))
