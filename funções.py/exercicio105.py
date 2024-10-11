def notas(*n, sit=False):
  """
  -> Função para analizar notas e situações de varios alunos.
  :Param n: uma ou mais notas dos alunos.
  :Param sit: valor opcional indicando se deve ou não indicar a situação.
  :Return: dicionário com várias informações sobre a turma.
  """
  r = dict()
  r["total"] = len(n)
  r["maior"] = max(n)
  r["menor"] = min(n)
  r["media"] = sum(n)/len(n)
  if sit:
    if r["media"] >= 7:
      r["situação"] = "BOA"
    elif r["media"] >= 5:
      r["situação"] = "RAZOAVEL"
    else:
      r["situação"] = 'RUIM'
  return r


# programa princiapl:
resp = notas(10, 9, 9, sit=True)
print(resp)
print(notas.__doc__)