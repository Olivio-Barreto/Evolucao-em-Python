print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Qual valor vpcê quer sacar? R$'))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV')