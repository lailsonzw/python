#META: montar um codigo que mostre a dimensao da parede, calcule os metros quadrados de uma parede e depois mostrar o tanto de tinta que sera necessario para pintar a parede;
#Obs precisamos de 1lt de tinta para pintar 2 metros de parede;


altura = float(input('Digite a altura da parede em metros:'))
largura = float(input('Digite a largura da parede em metros'))
area = altura * largura
tinta = area/2
preco = tinta * 10

print('A dimensao da parede e de {}x{}'.format(altura, largura))
print('A área de sua parede e de {}m²'.format(area))
print('Será gasto {}l de tinta para pintar sua parede por completo'.format(tinta))
print('Será gasto {:.4}$'.format(preco))
confirmacao = input('confirmar\nsim ou nao\ndigite aqui: ')
