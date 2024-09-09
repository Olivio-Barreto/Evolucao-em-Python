# TABOADA V2.0:
num = int(input('Digite um número para ver sua taboada: '))
for c in range(1, 10+1):
    print('{} x {:2} = {}'.format(num, c, num*c))