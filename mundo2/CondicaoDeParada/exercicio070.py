ProductName = str
price = float

MaisBarato = 100.00
NameMaisBarato = str
MaisDeMil = 0.0

total = 0.0

print('LOJA GUANABARA!')
while True:
   
    ProductName = str(input('Products name: '))
    price = float(input('Products price: '))
    
    total = price + total
    
    if price > 1000:
        MaisDeMil += 1
    
    elif MaisBarato > price:
        MaisBarato = price
        NameMaisBarato = ProductName

    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta.upper() == "N":
        break

print(f'O total da compra foi {total}R$. Temos {MaisDeMil} produtos custando mais de 1.000R$ e o produto mais barato da compra foi {NameMaisBarato}, custando {MaisBarato}R$.')
    
    
    