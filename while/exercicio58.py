from random import randint
computador = randint(1, 10)
print('Sou seu computaodr... Acabei de pensar em um número de 0 a 10.')
print('Consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez!')
        elif jogador > computador:
            print('Menos.. Tente mais uma vez!')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
