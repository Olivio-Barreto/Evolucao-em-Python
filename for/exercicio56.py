# Analizador completo:
# Variáveis
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = 0
total_mulher_20 = 0

# Formulários de dados pessoais
for p in range(1, 4+1):
    print('---- {}ª pessoa ----'.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('[M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm'and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

# Resultado do porgrama
media_idade = soma_idade / 4
print('A média da idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao total são {} mulheres com menos de 20 anos'.format(total_mulher_20))