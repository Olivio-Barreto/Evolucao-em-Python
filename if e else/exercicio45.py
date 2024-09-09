# GAME: Pedra, papel, tesoura:
from random import randint
#jogador = str(input("Digite Pedra, Papel ou tesoura:"))

itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual vai ser sua jogada? '))
print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:     # computador jogou pedra

    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você VENCEU!')
    elif jogador == 2:
        print('Você PERDEU!')
    else:
        print('Jogada inválida!')
elif computador == 1:   # computador jogou papel

    if jogador == 0:
        print('Você PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você GANHOU!')
    else:
        print('Jogada inválida!')
elif computador == 2:   # computador jogou tesoura

    if jogador == 0:
        print('Você VENCEU!!')
    elif jogador == 1:
        print('Vocë PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')