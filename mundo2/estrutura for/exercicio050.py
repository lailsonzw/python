#META: Criar um progama que leia seis numero inteiros e depois some apenas os numeros par;

numeros = list(range(0,6))
soma = 0

for ordem in range(0,6,1):
    print('Digite um valor para o vetor[{}]: '.format(ordem))
    numeros[ordem] = int(input(''))
    if numeros[ordem]%2 == 0:
        soma = soma + numeros[ordem]

print('A soma dos numeros pares foi {}'.format(soma))