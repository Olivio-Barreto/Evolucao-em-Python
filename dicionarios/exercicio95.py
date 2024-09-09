cadastro = {
    "nome": str(input("Nome: "))
}
lista_gols = list()
cadastro["quant_partidas"] = int(input(f"Quantas partidas {cadastro['nome']} jogou?"))
if cadastro["quant_partidas"] != 0:

    for i in range(0, cadastro["quant_partidas"]):
        cadastro["gols"] = int(input(f"Quantos gols na partida {i}?: "))
        lista_gols.append(cadastro["gols"])

    cadastro["gols"] = lista_gols

    for gol in lista_gols:
        cadastro["total"] = gol + gol

print("-="*40)
print(cadastro)
print("-="*40)
for k, v in cadastro.items():
    print(f"O campo {k} tem valor: {v}")
