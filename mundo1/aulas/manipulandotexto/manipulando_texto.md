Aula-09

    nesta aula iremos aprender:
    -Cadeias de caracter ou manipulando cadeias de textos;

O que são cadeias de caracter:
    
    -É a forma em que os caracteres são armazenados na variavel;
       
        Quando adicionamos uma frase dentro de uma variavel ela automaticamente e separada em microespaços na memoria do compultador
            por exemplo: frase = 'test' é armazenada da seguinte forma: [t][e][s][t], logo a frase teste ocupa 4 bites de memoria;
                                                                        0   1   2   3
    
    -Podemos manipular apenas uma letra dentro dessa frase, isto se chama fatiamento e fuciona da seguinte maneira;
        
        imprimindo apenas um valor da frase: print(frase[0]), vai amostrar apenas o valor que está armazenado no valor 0 que é o "t";
        
        como manipular apenas um local da frase: frase[3] = input('troque o valor do caracter do vetor 3'), ao fazer isso iremos trocar apenas o caracter do espaço 3;
            exemplo: frase[3] = input('troque o valor do caracter do vetor 3'), se eu colocar a letra "a", quando fomos imprimir o valor da variavel frase tera o seguinte resultado: print(frase) = "teat";
        
        podemos tambem escolher o tanto que queremos imprimir algo da seguinte forma: print(frase[2]) = imprima o conteudo de 0 ate 2 da frase, seu resultado será: "te";

        tipos de fatiamentos no python3:

        1- print(frase[1]) = imprime apenas o caracter do endereço 1;
        2- print(frase[1:3]) = imprime do endereço 1 ate o 2;
        3- print(frase[1:]) = imprime do endereço 1 ate o ultimo endereço;
        4- print(frase[:5]) = imprime do endereço 0 ate o endereço 5;
        5- print(frase[0:5:2]) = imprime do endereço 0 ate o endereço 5 pulando duas em duas casas, resultado = "ts"

        Funções para analise de string:
        
        1- len(frase) = mostra a quantidade de caracter de uma função;
        2- frase.count('t') = conta quantos "t" existem na função;
        3- frase.find('tes') = verifica se existe a palavra digitada retornando TRUE or FALSE;

        Transformação de string:
            
            Metodos para manipular string:
            
            1- frase.replace('t','p') = irar SUBISTITUIR o valor selecionado pelo valor digitado apos a virgula, resultado = "pesp";
            2- frase.upper() = irar deixar as letras que eram minusculas em maiusculas;
            3- frase.lower() = faz o inverso do upper;
            4- frase.capitalize() = irar deixar todas as letras em minusculas e depois deixara apenas a primeira letra em maiuscula;
            5- frase.title() = irar deixar apenas as letras entre os espaços maiusculas;
            6- frase.strip() = remove todos os espaços inuteis;
                -frase.rstrip() = remove apenas os espaços inuteis do lado direito;
                -frase.lstrip() = remove apenas os espaçoes inuteis do lado esquerdo;
            
        Divisoes destring

            metodos para dividir strings;

            1- frase.split() = irar uma fazer divisao de caracter entre os espaços;
            2- 'qualquer_coisa'.join(frase) = irar substituir os espaços vazios pelo valor digitado entre as aspas;
            3- frase.strip() = remove os espaços desnecessarios;
