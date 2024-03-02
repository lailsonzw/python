#META: crie um progama parecido com exercicio anterior, mas com uma condição, verificar se o usuario está digitando o sexo corretamente;

#Variavel criada para guardar a quantidade de homens;
sexoMasculino = 0
#Variavel criada para guardar a quantidade de Mulheres;
sexoFeminino = 0

#Variavel criada para armazenar a quantidade de pessoas
quantidade = int(input('digite a quantidade de pessoas que irão participar: '))

ordem = 0

while ordem < quantidade:
   
    pergunta = str(input('Digite o sexo desse usuario\nsexo [M/F]: '))
   
    if pergunta.upper() != "F" and pergunta.upper() != "M":
     
        while pergunta.upper() != "F" and pergunta.upper() != "M":
            pergunta = str(input('Parece que voce digitou errado, tente novamente: '))
    else:
      
        if pergunta.upper() == "F":
            sexoFeminino = sexoFeminino + 1
        
        elif pergunta.upper() == "M":
         sexoMasculino = sexoMasculino + 1
    
    ordem += 1
    
print('O total de homens foi de {}'.format(sexoMasculino))
print('O total de mulheres foi de {}'.format(sexoFeminino))