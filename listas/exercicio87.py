matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_colunas = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}], [{c}]: "))

print("=" * 30)
for l in range(0, 3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        
    print()
print('=' * 30)
print(f'A soma dos valores pares é {soma_pares}')
for l in range(0,3):
    soma_colunas += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {soma_colunas}")
for c in range(0, 3):
    if c == 0:
        maior = matriz[l][c]
    elif matriz[l][c] > maior:
        maior = matriz[l][c]