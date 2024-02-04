#Criar um progama que faça o alistamento militar;
from os import system

idade = int(input('Digite o ano que você nasceu\nAno: '))
verificacao = 2023 - idade
system('clear')

if verificacao == 18:
    print('\033[1;32;40mverificado com sucesso')
    nome = str(input('\033[0;0;0mdigite seu nome: '))
    cidade = str(input('digite aonde voce nasceu: '))
    system('clear')
    print('===DADOS===\nNome: {}\nIdade: {}\nLocal onde nasceu: {}\nSituação atual: \033[1;32;40mAlistado\n\033[0;0;0m===========\n'.format(nome,2023-idade,cidade))
elif verificacao > 18:
    print('\033[1;33;40mALERTA\033[0;0;0m')
    print('quem nasceu em {} tem {} anos. Você já deveria ter se alistado há {} anos'.format(idade, 2023 - idade ,(2023 - idade) - 18))
    nome = str(input('digite seu nome: '))
    cidade = str(input('digite aonde voce nasceu: '))
    system('clear')
    print('===DADOS===\nNome: {}\nIdade: {}\nLocal onde nasceu: {}\nSituação atual: \033[1;32;40mAlistado\n\033[0;0;0m===========\n'.format(nome,2023-idade,cidade))
elif verificacao < 18:
    print('\033[1;31;40mERROR!!!')
    print('quem nasceu em {} tem {} anos. Você ainda não pode se alistar, pois não tem 18 anos, você só pode fazer o alistamento daqui a {} anos'.format(idade, 2023 - idade,18 - (2023 - idade)))
  