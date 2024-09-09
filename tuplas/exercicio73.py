times = ('Corinthians', 'Palmeiras', 'Bahia', 'Vitória', 'Grêmio', 
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Bota fogo')


print('-='*15)
for t in times:
    print(t)
print('-='*15)
print(f'Os 5 primeiros são: {times[0:6]}')
print('-='*15)
print(f'os 4 últimos são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index('Chapecoense')}ª posição')