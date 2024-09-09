aluno = {
   "nome": str(input("Digite seu nome: ")),
   "media": float(input("Média do aluno: "))
}

if aluno["media"] >= 7:
    aluno["situação"] = 'Aprovado!'
elif 5 <= aluno["media"] < 7:
    aluno["situação"] = 'Recuperação!'
else:
    aluno["situação"] = 'Reprovado!'

for k, v in aluno.items():
    print(f"  - {k} é {v}")

