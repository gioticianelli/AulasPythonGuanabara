'''
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo.
'''


#Condição para a existência de um triângulo:
# a soma dos comprimentos de quaisquer dois lados de um triângulo deve ser sempre maior que o comprimento do terceiro lado

r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possivel formar um triângulo')
else:
    print('Não é possível formar um triângulo')