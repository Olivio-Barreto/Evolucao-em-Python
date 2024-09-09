soma = 0
conte = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        conte = conte + 1
        soma = soma + c
print(f'A soma de todos os {conte} valores solicitados é {soma}')
