numeros = list()

while True:
    # pede ao usuario um valor
    n = int(input("Digite um valor: "))
    # se o valor nao estiver na lista, ele é incluido. Caso contrário, não é
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado!")
    else:
        print("Valor duplicado. Não é possível adiciona-lo!")
    # pergunta se o usuario quer continuar
    resposta = str(input("Quer continuar?[S/N]: "))
    # se a pergunta do usuario for 'N' ou 'n' o programa é encerrado
    if resposta in 'Nn':
        break
print('='*30)
# coloca os numeros em ordem
numeros.sort()
print(f'Você digitou os valores {numeros}')