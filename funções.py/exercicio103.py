def Ficha(jog='<desconhecido>', gol=0):
    if jog == '':
        jog = "<desconhecido>"
    print(f'O jogador {jog} fez {gol} gols')

#Programa principal:
n = str(input("Nome do jogador: "))
g  = str(input("Numero de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip == '':
    Ficha(gol=g)

Ficha(n, g)