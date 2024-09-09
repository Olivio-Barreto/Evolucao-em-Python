total_18 = total_man = total_women = 0


while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        total_18 += 1
    if sexo == 'M':
        total_man += 1
    if sexo == 'F' and idade < 20:
        total_women += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com 18 anos: {total_18}')
print(f'Ao todo temos {total_man} homens cadastrados')
print(f'E temos {total_women} mulheres com menos de 20 anos')