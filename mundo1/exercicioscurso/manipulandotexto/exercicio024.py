#META: crie um progama que verifique se a cidade digita começa com "santo"

cidade = str(input('Digite o nome da cidade em que você nasceu: ')).strip("")
print(cidade[:5].upper() == 'SANTO')