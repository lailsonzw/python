#META: criar um progama que realize contagens regressivas;
from time import sleep

contagem = int(input('quanto tempo será a contagem?\ntempo: '))
tempo = contagem
for c in range(contagem,-1,-1):
    
    print('TEMPO RESTANTE: {}'.format(tempo))
    sleep(1)
    tempo = tempo -1
    
