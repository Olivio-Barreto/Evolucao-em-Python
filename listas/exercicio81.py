valores = []
while True:
    valores.append(int(input("digite um valor: ")))
    resposta = str(input("Quer continuar?[S/N]: ")).upper()
    if resposta in "N":
        break
print('~^'*30)
print(f"Você digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O número 5 está na lista!")
else:
    print("O número 5 não está na lista!")