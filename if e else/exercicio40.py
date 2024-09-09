# CALCULANDO A MÉDIA:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print('O aluno está REPROVADO.')
elif media >= 5.0 and media < 7.0:
    print('O aluno fará a RECUPERAÇÃO.')
elif media >= 7.0:
    print('O aluno está APROVADO!')
