#META: faça um progama que almente o salario do trabalhador, se o salario for menor que 1.000$ aumente 15%, se não aumente 10%;


salario = float(input('digite o salario do funcionario: '))
valoralto = 1000

if salario > valoralto:
    print('O salario que custava {}, passou a custar {}'.format(salario, salario + (10/100 * salario)))
else:
    print('O salario que custava {}, passou a custar {}'.format(salario, salario + (15/100 * salario)))

    