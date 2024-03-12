count = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
         'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    
    if 0 <= num <= 20:
        break
    
    print('Tente novamente.')

print(f'O nomero que voce digitou foi {count[num - 1]}')
        