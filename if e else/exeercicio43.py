#ÍNDICE DE MASSA CORPORAL:
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC  dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc > 18.5 and imc < 25:
    print('PARABÉNS, você está na FAIXA de PESO normal.')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')
elif imc >=30 and imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
