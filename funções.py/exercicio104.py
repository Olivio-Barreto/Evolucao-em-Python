def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro.\033[m")
        if ok:
            break
    return valor

# programa principal
n = leiaInt(10)
print(n)