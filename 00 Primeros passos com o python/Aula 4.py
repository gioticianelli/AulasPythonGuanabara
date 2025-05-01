#Desafio 1
nome = input('Qual o seu nome?')

print('Olá', nome, '! Prazer em te conhecer!' )

#Desafio 2
print('Qual a sua data de nascimento?')

dia = int(input('Dia de nascimento: '))
mes = int(input('Mês de nascimento: '))
ano = int(input('Ano de nascimento: '))
ano_atual = 2025
idade = (ano_atual - ano)


print('Você tem ', idade, ' pois nasceu', dia,'de', mes,'de', ano)

#Desafio 3
num1 = float(input('Digite o 1° núemro: '))
num2 = float(input('Digite o 2° número: '))
soma = (num1 + num2)

print('A soma dos seus número é: ', soma)