'''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Quanto é o seu salário? '))

if salario <= 1250:
    aumento = (15/100) * salario
    novo_salario = salario + aumento
    print('O seu salário teve aumento de 15%.\nAgora você recebe R${}'.format(novo_salario))
else:
    novo = salario + (salario * 10 / 100)
    print('O seu slário teve aumento de 10%.\nAgora você recebe R${}'.format(novo))
