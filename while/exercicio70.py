total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('NOmde do produto: '))
    preço = float(input('Preço R$: '))
    cont += 1
    total += preço
    if preço > 1000:
         totmil += 1
    if cont == 1:
         menor = preço
    else:
         if preço < menor:
              menor = preço
              barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
            break
print('Acabou!')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')