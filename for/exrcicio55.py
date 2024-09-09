# MAIOR e MENOR da sequência:
maior = 0
menor = 0
for p in range(1, 5+1):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = p
        manor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))
