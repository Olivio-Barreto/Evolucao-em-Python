# MAIOR E MENOR VALORES:
from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
# Verificando qual é o menor:
if b < a and b < c:
    menor = b
if c < a and c < a:
    menor = c
print('Analisando...')
sleep(2)
print(f'O menor valor é {menor}')
# Verificando qual é o maior:
a = int(input('primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('Analisando...')
sleep(2)
print(f'O maior valor é {maior}')