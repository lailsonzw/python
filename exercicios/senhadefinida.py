#META: criar um comando que permita o usuario criar uma senha e depois efetuar o login;

senha = input("Digite a senha do menu:")

print("---MENU---")
usuariosenha = input("Digite a senha para entrar no progama:");
print("----------")

if usuariosenha == senha: 
    print("Senha correta")
else:
    print("senha incorreta")