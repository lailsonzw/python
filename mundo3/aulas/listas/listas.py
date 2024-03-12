#listas são parecidas com tuplas em python, mas sua principal diferença para as tuplas é que as tuplas não são modificas, já as listas podem ser podificadas;

#Adicionando elementos na lista:

    #usando a função append('valor') podemos adicionar um novo elemento  no final da lista;

    #insert(posicao, 'valor') serve para adicionar um elemento na posição desejada diferente do append();

    #exemplo: insert(0, 'test') irar adicionar test no inicio da lista e pasara o elemento que estava no 0 para a posicao 1;

#Deletando elementos na lista

    #para remover elementos da lista podemos usar a função NameList.pop(posicao)
    #ou
    #del lanche[posicao]
    #ou
    #lanche.remove(valor)

#Organização de elementos

    #lista = [1,2,4,5,7,3,8,9]
    
    #Para organizar essa lista podemos usar a função sort();
    
    #Exemplo: lista.sort() -> irar organizar os numeros em ordem crescente
    
    #Exemplo: lista.sort(reverse = True) -> irar organizar os elementos em ordem decrecesente
        
#Hora da pratica
    
lista = [4, 2, 1]
lista.append(3)
lista.pop(2)
print(f'Quantidade de itens na lista {len(lista)}, Valores da lista {lista}, lista em ordem {lista.sort()}')
