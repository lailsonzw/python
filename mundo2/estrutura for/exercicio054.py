#META: monte um progama que verifique a quantidade de pessoas que são de maior;

quantidade = int(input('Digite a quantidade de usuarios que terão no progama: '))
maiores = 0
menores = 0 

for ordem in range(quantidade):
    ano = int(input('Digite o ano que você nasceu: '))
    confirmacao = 2023 - ano
    if confirmacao > 17:
        maiores = maiores + 1
    else: 
        menores = menores + 1

print("Das {} pessoas intrevistadas, {} são maiores de idade e {} são menores de idade.".format(quantidade, maiores, menores))