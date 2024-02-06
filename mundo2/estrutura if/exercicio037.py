#META: criar um convensor de numeros, o progama pegara um numero inteiro e irar poder ser convertido para binario,hexadecimal,octal a partir da escolha do user;

print("\033[1;0;0mBem vindo ao conversor de numeros")
numint = int(input('Digite um valor inteiro: '))
print('1-binario 2-hexadecimal 3- octal')
conversao = int(input("Digite o valor que o numero será convertido: "))

if conversao == 1:
    conversao = bin(numint)
    print('numero inteiro: {}, numero em binario: {}'.format(numint, conversao[2:]))
elif conversao == 2:
    conversao = hex(numint)
    print('numero inteiro: {}, numero em hexadecimal: {}'.format(numint, conversao[2:]))
else:
    conversao = oct(numint)
    print('numero inteiro: {}, numero em octal: {}'.format(numint, conversao[2:]))

    
