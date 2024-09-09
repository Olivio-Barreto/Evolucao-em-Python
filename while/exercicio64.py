num  = 0
cont = 0
soma = 0
num = int(input('Digite um número, [999 PARA PARAR!]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número, [999 PARA PARAR!]: ')) 
print(f'Você digitou {cont} números e a soma entre eles foi de {soma}!')
