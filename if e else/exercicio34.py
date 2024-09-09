# AUMENTOS MÚLTIPLOS:
salário = float(input('Qual seu salário? '))
if salário <= 1250:
    novo = salário + (salário * 15) / 100
    print(f'Você recebeu um aumento de 15%, seu soldo ficará em R${novo}')
if salário > 1250:
    novo = salário + (salário * 10) / 100
    print(f'Você recebeu um aumento de 10%, seu soldo ficará em {novo}')
