#META: Criar um progama que mostre a pessoa mais pesada e a mais leve em uma lista, o usuario quem deve escolher a quantidade de pessoas;

quantidade = int(input('Digite a quantidade de pessoas que irao participar: '))

maiorPeso = 0.0
menorPeso = 10000000

for p in range(0, quantidade):
    pesoAtual = int (input('digite o peso: '))
    if maiorPeso < pesoAtual:
        maiorPeso = pesoAtual
   
    if menorPeso > pesoAtual:
        menorPeso = pesoAtual
        
print('Dos {} participantes o maior peso obtido foi de {} e o menor foi de {}'.format(quantidade, maiorPeso, menorPeso))
    
        
