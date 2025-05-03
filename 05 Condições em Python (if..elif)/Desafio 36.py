'''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual o salário do comprador? R$'))
financiamento = int(input('Quantos anos de financiamento? '))
prestacao = casa / (financiamento * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, financiamento, prestacao))

if prestacao <= minimo:
    print('O empréstimo pode ser CONCEDIDO')
else:
    print('O empréstimo vai ser NEGADO')
