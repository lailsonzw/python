#META criar um progama que verifique se a senha e correta;


password = str("101270")#variable que vai guardar a password do user;
passworduser = str()#variable que irar guardar o valor que o user digitar;

print("Digite a senha:")
passworduser = input()

if passworduser == password:
    print("senha correta")

else:
    print("senha errada")