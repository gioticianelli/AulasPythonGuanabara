'''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input('Digite um número: '))
print('Escolha uma base para conversão:\n'
      '[1] BINÁRIO\n'
      '[2] OCTAL\n'
      '[3] HEXADECIMAL')
base = int(input('Digite a base escolhida: '))
if base == 1:
   binario = bin(num)[2:]
   print('{} convertido para BINÁRIO é igual a {}'.format(num, binario))
elif base == 2:
    oct = oct(num)[2:]
    print('{} convertido para OCTAL é igual a {}'.format(num, oct))
elif base == 3:
    hexa = hex(num)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexa))
else:
    print('Não há essa opção.')






