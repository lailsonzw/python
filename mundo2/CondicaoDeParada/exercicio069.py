MaioresDeIdade = 0
mulheres = 0 
homens = 0 

while True:
    
    print('Cadastro de pessoa\n')
    
    idade = int(input('Digite a idade da pessoa:'))
    sexo = str(input('digite  o sexo da pessoa, [M/F]: '))
    
    if sexo.upper() == "M":
        homens += 1
    elif sexo.upper() == "F":
        mulheres += 1

    if idade >= 18:
        MaioresDeIdade += 1
    
    resposta = str(input('Quer continuar?\n[S/N]: '))
    
    if resposta.upper() == "N":
        break

print(f'Ao total tivemos {MaioresDeIdade} maiores de idade, {homens} homens e {mulheres} mulheres.')
    