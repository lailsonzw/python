#META: calcular o preço da passagem, se a passagem for menos de 200km cobre 0.50, se for mais, cobre 0.45;


distancia = int(input('Digite a distancia em km da sua passagem. Caso a distancia ultrapasse 200km voce ganhara disconto: '))

if distancia > 200:
    preco = distancia * 0.45
    print('Voce ganhou disconto')
    print('Total: {}'.format(preco))
else:
    preco = distancia * 0.50
    print('Total: {}'.format(preco))    