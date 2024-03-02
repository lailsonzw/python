#META, crie um progama que leia vários numeros inteiros pelo teclado. No final da execução, mostre a soma desses numeros o maior numero digitado e o menor
Resposta = 'S'
soma = total = RMedia = MaiorNum = MenorNum = 0
while Resposta in 'Ss':
     
    Ndigitado = int(input('digit a number: '))
    soma += Ndigitado
    total += 1
     
    if total == 1:
        MaiorNum = MenorNum = Ndigitado
    
    else:
        if MaiorNum < Ndigitado:
            MaiorNum = Ndigitado
        if MenorNum > Ndigitado:
            MenorNum = Ndigitado
    
    Resposta = str(input('Voçê quer continuar? s ou n: ')).upper().strip()[0]
    
RMedia = soma/total
print('A média dos números foi {}. O maior número digitado foi {} e o menor foi {}'.format(RMedia, MaiorNum, MenorNum))
    