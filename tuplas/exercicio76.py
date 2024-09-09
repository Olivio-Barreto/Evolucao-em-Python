listagem = ('lápis', 1.75,
            'borracha', 2,
            'cadernp', 15.90,
            'estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.90,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('•' * 40)
print('LISTAGEM')
print('•' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:5.2f}')
print('•' * 40)
