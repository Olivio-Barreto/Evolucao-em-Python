# RADAR ELETRÔNICO:
velocidade = float(input('Digite a velocidade atual em Km: '))
if velocidade > 80:
    print('MULTADO, você excedeu o limite permitido que é 80Km/h')
    multa = (velocidade-80) * 7
    print(f'Você tem que pagar uma multa de R${multa}')
print('Tenha um bom dia!, Dirija com seguranca!')
