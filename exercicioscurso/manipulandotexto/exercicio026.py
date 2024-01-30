#META: criar um progama que mostre quantas vezes a letra 'A' aparace na frase;
#-Quando apareceu a primeira vez;
#-Quando apareceu a ultima vez;

frase = str(input('digite uma frase: \n')).strip()

print('A letra "a" aparece {} vezes na frase'.format(frase.count("a")))
print('A letra "a" aparece pela primeira vez na posição: {}'.format(frase.find('a')+1))
print('A letra "a" aparece pela ultima vez na posição {}'.format(frase.rfind("a")+1))

#funcao "var.find("letra")" mostra aonde a letra digitada pelo usuario aparece a primeira vez na variavel;
#função "var.rfind("letra")" mostra aonde a letra digitada pelo usuario aparece pela ultima vez na variavel;