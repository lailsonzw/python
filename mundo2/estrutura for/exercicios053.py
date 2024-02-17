#META: Criar um codigo que pegue uma frase e depois motre se ela tem palidromo;


frase = str(input("Digite uma frase: "))
frase_s_espaco = frase.replace(' ','')
frase_invertida =  frase_s_espaco[::-1]
confirmacao = frase_s_espaco

print('Dados\n')
print('Frase normal: {}'.format(confirmacao))
print('Frase invertida: {}\n'.format(frase_invertida))

if confirmacao.upper() == frase_invertida.upper():
    print('Essa frase é um palindromo.')
else:
    print('Essa frase não é um palindromo.')
