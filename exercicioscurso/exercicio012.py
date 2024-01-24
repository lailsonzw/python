#META: criar um codigo que receba um valor e aplique um disconto dele, de preferencia leia o valor do desconto;

valordoproduto = int(input('Quanto custa o produto: '))
tamanho = int(input('Diga qual vai ser o tamanho do desconto: '))
desconto =  (valordoproduto * tamanho)/100
valor_final = valordoproduto - desconto

print('Seu produto custava {}$, mas com o desconto de {}% ele passa a custar {}$'.format(valordoproduto, tamanho, valor_final))