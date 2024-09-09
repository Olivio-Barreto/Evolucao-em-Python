# TUPLAS

cont = ('Zero', 'um', 'dois', 'tres', 'quatro', 'cinco' 'seis'
        , 'sete', 'oito', 'nove', 'dez')


while True:
    num = int(input('Digite um numero entre 0 e 10: '))
    if num >=0 and num <= 10:
        break
    print('Tente novamente!', end=' ')
print(f'Você digitou o número {cont[num]}')