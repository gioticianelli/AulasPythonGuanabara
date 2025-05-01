velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Você foi multado. O limite permitido era de 80km/h')
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R${:.2f} '.format(multa))
print('DIGIRA COM SEGURANÇA!')