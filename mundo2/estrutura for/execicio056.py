#META: criar um progama que mostre a media da idade dos usuarios, mostrar o homem mais velho e a mulher mais velha;

N_homem_mais_velho = 0
N_mulher_mais_velha = 0

maiorIdadeH = 0
maiorIdadeF = 0

somaIdade = 0
media = 0

quantidade = int(input('Digite a quantidade de usuarios que irão participar: '))

for ordem in range(0,quantidade):
    print('---{} pessoa---'.format(ordem+1))
    nome = str(input('Digite seu nome: '))
    idade = int(input('diga sua idade: '))
    sexo = str(input('diga seu sexo [M/F]\nsexo: '))
    
    somaIdade += idade 
    
    if sexo.upper() in "M" and idade > maiorIdadeH:
        maiorIdadeH = idade
        N_homem_mais_velho = nome
    
    if sexo.upper() in "F" and idade > maiorIdadeF:
        maiorIdadeF = idade
        N_mulher_mais_velha = nome

media = somaIdade / quantidade

print('Todos os dados foram preenchidos!')
print('O homem mais velho se chama {} e tem {} anos'.format(N_homem_mais_velho,maiorIdadeH))
print('A mulher mais velha se chama {} e tem {} anos'.format(N_mulher_mais_velha,maiorIdadeF))
print('A media das idades foram de {:.2f} anos'.format(media))