# SEQUÊNCIA FIBONACCI:
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos você quer mostrar? '))
termo_1 = 0
termo_2 = 1

print('~' * 30)
print(f'{termo_1} -> {termo_2}', end='')
cont = 3
while cont <= n:
    termo_3 =  termo_1 + termo_2
    print(f' -> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    cont += 1
print(' -> FIM!')