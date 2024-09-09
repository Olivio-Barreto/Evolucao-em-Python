num = []
list_par = []
list_impar = []
while True:
    num.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar?[S/N]: ")).upper()
    if resposta in "N":
        break
    if not resposta in "NS":
        print("Não entendi sua resposta")
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        list_par.append(v)
    elif v % 2 == 1:
        list_impar.append(v)
print(f"A lista completa tem os valores {num}")
print(f"A lista com números pares tem os valores {list_par.sort()}")
print(f"A lista com valores ímpares tem os valores {list_impar.sort()}")