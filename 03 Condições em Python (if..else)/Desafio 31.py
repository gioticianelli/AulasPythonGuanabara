'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distancia = int(input('Qual a distância da viagem?(Informe a distância em Km): '))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print('Para a viagem de {}km, você irá pagar pela passagem R${:.2f}'.format(distancia, passagem))
print('Boa viagem!!')
