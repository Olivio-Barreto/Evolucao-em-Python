pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))

    while True:
        pessoa["sexo"] = str(input("Digite seu sexo [M/F]: "))
        if pessoa["sexo"] not in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")

    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())

    while True:
        resposta = str(input("Quer continuar? [S/N]: ")).capitalize()
        if resposta in 'SN':
            break
        if resposta not in 'SN':
            print("ERRO! Por favor, digite apenas S ou N.")
            break

    if resposta == 'N':
        break
media = soma / len(galera)      

print(pessoa)
print(galera)
print(media)