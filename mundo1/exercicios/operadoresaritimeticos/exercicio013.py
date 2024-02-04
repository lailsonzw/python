#META: fazer um reajuste salarial no salario do funcionario, faça isso usando porcentagem;

#Coletando o salario e o quanto o salario vai aumentar;
salario = float(input('Digite o salario do funcionario:'))
reajuste = int(input('quantos por cento o salario do funcionario irar aumentar?\nDigite aqui:'))


reajuste = (salario*reajuste)/100
novo_salario = salario + reajuste

print('O salario do funcionario custava {}, mas com o novo reajuste passou a custar: {}'.format(salario, novo_salario))

 