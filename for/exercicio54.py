from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0
for pess in range(1, 7+1):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '))
    idade = atual - nasc

    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('Tivemos {} pessoas maiores de idade'.format(total_maior))
print('E tivemos {} pessoas menores de idade'.format(total_menor))

