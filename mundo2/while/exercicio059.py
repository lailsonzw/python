#META: Crie um progama que leia dois valores e mostre um meno na tela:
import os

num1 = int(input('Digite o um valor para um numero: '))
num2 = int(input('Digite o um valor para o segundo numero: '))
os.system("clear")

resultado = 0

escolha = 0

while escolha != 5:
    print('MENU\n\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do progama\n')
    escolha = int(input('escolha uma opção: \n'))
    os.system("clear")
    
    if escolha == 1:
        resultado = num1 + num2
        print('A soma dos numeros deram {}\n'.format(resultado))

    elif escolha == 2:
        resultado = num1 * num2
        print('A multiplicacao dos numeros deram {}\n'.format(resultado))
    
    elif escolha == 3: 
        if num1 > num2:
            print('O maior número é {}\n'.format(num1))
        elif num1 == num2:
            print('Os números são iguais.\n')
        elif num2 > num1:
            print('O maior número é {}\n'.format(num2))

    elif escolha == 4:
        num1 = int(input('Digite um novo valor para o primeiro número: '))
        num2 = int(input('Digite um novo valor para o segundo número: \n'))
    