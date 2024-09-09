# APROVANDO EMPRÉSTIMO:
casa = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: '))
anos = int(input('Quantos amos de financiamento: '))
prestação = casa / (anos * 12)
mínimo = salário * 30/100
print('Para pagar a casa de R${} em {} anos,'.format(casa, anos), end='')
print(' a prestação da casa será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Seu empréstimo foi aprovado! APROVEITE!')
else:
    print('Empréstimo não permitido!')
