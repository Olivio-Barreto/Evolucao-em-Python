lista = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))
    # se for o primeiro valor, faz-se um append (adiciona à uma lista)
    if c == 0:
        lista.append(n)
    # se o valor for maior que o ultimo valor, tambem faz um append (adiciona à uma lista)
    elif n > lista[len(lista)-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
print('='*40)
print(f"Os valores digitados foram: {lista}")
print('='*40)