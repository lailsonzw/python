quantidade = 0
numero = 0
soma = 0

while True:
    numero = int(input('Digite um numero: '))
    soma = numero + soma
    quantidade += 1
    
    if numero == 999:
        break

soma -= 999
print(f"Você digitou {quantidade} numeros e a soma deles foi de {soma}")