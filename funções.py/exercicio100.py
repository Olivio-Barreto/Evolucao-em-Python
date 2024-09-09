from random import randint
# def sorteia():
def sorteia(lista):
    for v in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(lista)
#def somaPar():
def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)
numeros = list()
sorteia(numeros)
soma_par(numeros)