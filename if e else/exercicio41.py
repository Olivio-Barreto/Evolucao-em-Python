# CLASSIFICANDO ATLETAS:
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade} Anos')
if idade <= 9:
    print('Classificamção: MIRIM!')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
