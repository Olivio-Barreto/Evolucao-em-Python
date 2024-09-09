#cirar a fnção
import time
#passar os parametros
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} ao {f} de {p} em {p}')
        time.sleep(2)
        cont = i
        while cont <= f: #enquanto o inicio for menor ou igual ao fim
            print(f'{cont} ', end='', flush=True)
            cont += 1
            time.sleep(0.5)
        print('Fim!')  
    else:
        print(f'Contagem de {i} ao {f} de um {p} em {p}')
        time.sleep(2)
        cont = i
        while cont >= f: #enquanto o inicio for maior que o fim
            print(f"{cont}", end=' ', flush=True)
            cont -= p
            time.sleep(0.5)
        print("Fim!")
#contar os numeros
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 20)
print("Agora é sua vez de personalizar a sua contagem!")
ini = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(ini, fim, passo)

