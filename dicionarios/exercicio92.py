#declarando um dicionario
dados = dict()

dados["nome"] = str(input("Digite seu nome: "))#criando uma key e inserindo um input como valor

nasc = int(input("Digite o ano do seu nascimento: "))#requisição do ano de nascimento

# inclusão da biblioteca para requeisição automãtica da idade
from datetime import datetime
dados["idade"] = datetime.now().year - nasc

dados["ctps"] = int(input("Carteira de trabalho (0 não tem): "))#criando uma key(ctps) e inserindo um input como valor

if dados["ctps"] != 0:
    dados["contratacao"] = int(input('Digite o ano contratação: '))
    dados["salario"] = float(input("Salario: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - datetime.now().year)

print(dados["aposentadoria"])
print(dados)
for k, v in dados.items():
    print(f"{k} tem o valor {v}")