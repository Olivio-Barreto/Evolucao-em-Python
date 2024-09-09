# análise de dados em tupla:

num = (int(input('Digite um numero: ')), 
       int(input('Digite outro numero: ')), 
       int(input('Digite mais um numero: ')), 
       int(input('Digite o último numero: ')))
print(f'O numero 9 apareceu {num.count(9)} vezes!')
if 3 in num:
   print(f'O numero 3 está na posição {num.index(3)+1}')    
else:
     print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
       print(n, end=' ')
