# JOGO DA ADVINHAÇÃO V1.0:
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei?: '))  # jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS!, você acertou!')
else:
    print('RESPOSTA ERRADA. Tente novamente!')
