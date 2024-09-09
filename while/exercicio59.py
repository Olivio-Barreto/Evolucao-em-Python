n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qaul é sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação de {} x {} é igual a {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, O maior número é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
print('Fim do programa. volte sempre!')