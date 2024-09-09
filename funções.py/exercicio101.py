def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f"Com {idade} anos: NÃO VOTA!")
    elif idade >= 16 and idade < 18 or idade > 65:
        return print(f"Com {idade} anos: OPICIONAL!")
    else:
        return print(f"Com {idade} anos: VOTO OBRIGATÓRIO!")
    
r1 = voto(2007)