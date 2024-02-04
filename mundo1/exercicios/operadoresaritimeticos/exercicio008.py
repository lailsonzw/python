#META: criar um convensor de medidas;

metros = float(input('Digite uma distancia em metros:'))
print('A medida de {}m corresponde a\n'.format(metros))
print('A medida de {}km\n'.format(metros/1000))
print('A medida de {}hm\n'.format(metros/100))
print('A medida de {}dam\n'.format(metros/10))
print('A medida de {}dm\n'.format(metros*10))
print('A medida de {}cm\n'.format(metros*100))
print('A medida de {}mm\n'.format(metros*1000))
