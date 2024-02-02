#META: montar um progama que calcule o preco do aluguel de um automovel...

dias = float(input('Quantos dias o carro ficou alugado?\nSua resposta: '))
km = float(input('Quantos km o carro andou durante {} dias?\nSua resposta '.format(dias)))
valor_final = (dias * 60) + (km * 0.15)
print('O valor final foi de {}$. Volte sempre!'.format(valor_final))