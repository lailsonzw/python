#META criar uma calculadora que faça calculos de soma,subtração,multiplicação e divisão;

operation = str()#variable for the user to make the choice of operation;
resultado = 0;
num1 = 0;
num2 = 0;

print("Escolha um tipo de operacao: /, +, -, *")
operation = input()

print("digite o primeiro num:")
num1 = int(input())
print("digite o segundo num:")
num2 = int(input())


if operation == '-':
    resultado = num1 - num2
elif operation == '+':
    resultado = num1 + num2
elif operation == '*':
    resultado = num1 * num2
elif operation == '/':
    resultado = num1 / num2 
print(resultado)

