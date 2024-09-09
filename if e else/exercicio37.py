# CONVERSOR DE BASES NUMÉRICAS:
num = int(input('Digite um valor: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1: # eliminando o "0b" no resultado: [2:]
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2: # eliminando o "0o" no resultado: [2:]
    print(f'{num} covertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3: # eliminando o "0x" no resultado: [2:]
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente!')
