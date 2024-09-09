palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro'
            )

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais:', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra.upper():>1}', end=' ')
