#META: Crie um progama que leia vario numeros inteiros, o progama so vai parar quando o numero 999 for digitado, ao terminar o progama mostre a soma dos numeros anteriores;
cont = 0
soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while(numero != 999):
    soma = soma + numero
    numero = int(input('Digite um número [999 para parar]: '))
    cont += 1
print("voce digitou {} numeros e a soma entre eles foi {}".format(cont,soma))