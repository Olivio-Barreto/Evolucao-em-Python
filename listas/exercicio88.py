from random import randint

lista = []
jogos = []
print('='*40)
print('     JOGO DA MEGA SENA     ')
print('='*40)
quant_jogos = int(input("Quantos jogos você quer que eu sorteie?: "))
total_jogos = 1
while total_jogos <= quant_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos += 1

print(f"Os numeros sorteados foram {jogos}")
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')