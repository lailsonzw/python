from os import system

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atletico-Pr', 'Bahia', 'São Paulo', 'Fluminense','Sport Recife', 'Ec Vitória','Coritiba', 'Avaí', 'Ponte preta', 'Atletico-Go' )

system('clear')
print('=' * 30)
print('PLACAR DO BRASILEIRAO 2018')
print('=' * 30)
print(f'Quantidade de times: {len(times)}')
print(f'Top 5: {times[0:5]}')
print(f'Os últimos 4 colocados: {times[-4:-1]}')
print(f'Times organizados em ordem alfabetica: {sorted(times)}')
posicao = times.index('Chapecoense')
print(f'O time da chapecoense está na posição {posicao}')