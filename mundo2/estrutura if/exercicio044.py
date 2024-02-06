#META: elabore um progama que calcule o preco de um produto, leve em consideração seu preço e o metodo de pagamento;

print('======== LOJA ========')
preco = float(input('digite o preco das compras: '))
formadepagamento = int(input('digite uma forma de pagamento:\n[1]-cartao\n[2]-a vista\n'))

if formadepagamento == 1:
    parcelas = int(input('voce irar pagar em quantas parcelas?\nparcelas: '))
    if parcelas <= 2:
        print('Valor final: {}'.format(preco))
        print('Em {} parcelas fica {}'.format(parcelas, preco/parcelas))       
    elif parcelas >= 3:
        juros = (preco) + (20/100) * preco
        print('valor final: {}'.format(juros))
        print('Em {} parcelas fica {}'.format(parcelas, juros/parcelas))
        
elif formadepagamento == 2:
    desconto = preco - (10/100) * preco
    print('valor final: {}'.format(desconto))
    
else:
    total = 0
    print('opcao invalida, tente novamente')