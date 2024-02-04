#META: criar um progama que mostre o nome e o sobrenome da pessoa;

nomecompleto = str(input('Digite seu nome completo: \n')).strip().split()

print("Seu nome completo é: {}".format(nomecompleto))
print("Seu primeiro nome é: {}".format(nomecompleto[0]))
print("Seu ultimo nome é: {}".format(nomecompleto[len(nomecompleto) - 1]))