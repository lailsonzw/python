

while True:
    numero = int(input('Digite um número que deseja mostrar a tabuada: '))
    
    if numero < 0:
        print('Progama encerrado.\n')
        break;
    
    for ordem in range(11):
        resultado = numero * ordem
        print(f"{numero} x {ordem} = {resultado}")
    