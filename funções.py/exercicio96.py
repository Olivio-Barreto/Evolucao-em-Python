a = float(input("Largura (m): "))
b = float(input("Comprimento (m): "))


def calcular_area(x=a, y=b):
    result = x * y
    print(f'A área de um terreno {x}x{y} é de {result}m².')

calcular_area()