# ALISTAMENTO MILITAR:
from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você precisa se alistar!')
elif idade < 18:
    print('Ainda não é o tempo, aguarde a idade correta!')
else:
    print('Sua idade de alistamento está ultrapssada!')
