temp = []
princ = []

while True:
    temp.append(str(input("nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
            
    princ.append(temp[:])
    temp.clear()
    resposta = str(input("Quer continuar?[S/N]: ")).capitalize()
    if resposta in 'N':
        break
    if resposta not in 'NS':
        print("Não entendi sua resposta!")
        break

print("="*30)
print(f"Os dados forma {princ}")
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f"A maior peso foi {maior}Kg. Peso de ", end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi {menor}Kg. peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
