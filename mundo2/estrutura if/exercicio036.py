#Meta criar um progama que irar aprovar umm emprestimo para comprar uma casa;
#RESTRIÇOES - a prestação não pode ser mais que 30% do salario;


valordacasa = float(input('Quanto vai custar a casa?\nValor: '))
salario = float(input('Quanto voce ganha?\nSalario: '))
prestacoes = float(input('em quantas prestacoes voce irar pagar a casa?\nprestações: '))
print("\n\n")

financiamento = (valordacasa / prestacoes)
condicao = (30/100) * salario

print('Valor das prestações: {}'.format(financiamento))
if financiamento > condicao:
    print('\033[1;31;40mNão sera possivel efetuar o emprestimo, pois voce não tem condição de manter o emprestimo\n')
else: 
    print('\033[1;32;40mSEU IMPRESTIMO FOI REALIZADO COM SUCESSO')
    print('\033[0;0;0maperte enter para sair.')
    conf = input()


