print('BANCO LAILSON')

valor = int(input('Quantos reais voce quer sacar?\nValor: '))
total = valor

ValorCed = 50
TotalCed = 0

while True:  
    if total >= ValorCed:
       total -= ValorCed
       TotalCed += 1
    else:
        print(f'Total de {TotalCed} cedulas de {ValorCed}R$')
        
        if ValorCed == 50:
            ValorCed = 20
        
        elif ValorCed == 20:
            ValorCed = 10
        
        elif ValorCed == 10:
            ValorCed = 1
        
        TotalCed = 0
        
        if total == 0: 
            break
            
                   