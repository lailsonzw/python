#META: criar um codigo que de um disconto de a cordo com a forma de pagamento que o cliente vai escolher;
import os

produto = float(input('quantos reais custa o produto?\ndigite aqui:'))
os.system('clear')
formadepagamento = int(input('qual vai ser a forma de pagamento?\n1- cartao = 5% de desconto\n2- a vista = 15% de desconto\n3- Fiado = sem desconto\ndigite aqui:'))
os.system('clear')
desconto = 0
precofinal = 0

if formadepagamento == 1:
    desconto = (produto * 5)/100
    precofinal = produto - desconto
else: 
    if formadepagamento == 2:
        desconto = (produto * 15)/100
        precofinal = produto - desconto
    else:
        precofinal = produto - desconto

print('o preço final ficou: \033[1;33;40m{}\n'.format(precofinal))
confirmar = int(input('deseja confirmar?\n1-sim ou 2-não\nDigite aqui:'))
if confirmar == 2:
    print('compra cancelada.')


#novo comando aprendido os.system('comandos relacionados ao seu terminal')
#esse comando vem da blibioteca "os"