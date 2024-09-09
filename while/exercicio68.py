from random import randint
v = 0
while True:
    print('-='*30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*30)
    jogador = int(input('Digite um número: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0:]
    print(f'Você jogou {jogador} e o computador jogou {comp}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Parabés, Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Parabéns, Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')