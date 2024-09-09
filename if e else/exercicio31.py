# CUSTO DA VIAGEM:
distância = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}Km')
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua viagem é de R${:.2f}'.format(preço))
