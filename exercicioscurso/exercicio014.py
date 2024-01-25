#meta criar um progama que faca uma convensao de temperatura automatica para o usuario;


temperatura_graus = float(input('Iforme a temperatura em graus:'))
escolha = int(input('Escolha uma temperatura para converter: 1 - kelvin ou 2 - farhenheit\nSua resposta: '))

kelvin  = (temperatura_graus + 273)
farhenheit = (temperatura_graus * 1.8) + 32

if escolha == 1:
    print('Sua temperatura antes da conversao: {}c, sua temperatura depois da conversao para kelvin: {}k'.format(temperatura_graus, kelvin))
else:
    print('Sua temperatura antes da conversao: {}c, sua temperatura depois da conversao para farhenheit: {}f'.format(temperatura_graus, farhenheit)) 

