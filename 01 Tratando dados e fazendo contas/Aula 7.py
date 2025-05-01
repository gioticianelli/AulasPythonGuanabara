
#**Potenciação
#// Divisão inteira
#% Resto da divisão
#- Subtração
#+ Soma
#* Multiplicação
#/ Divisão
#-+%//*/**()**/*//%+-


print('8' * 4) #Faz o 8 aparecer 4 vezes

nome = input('Digite seu nome: ')
print('Que bom ter você aqui {:20}!'.format(nome)) # Faz com que o nome tenha mais caracteres
print('Que bom ter você aqui {:>20}!'.format(nome)) #Coloca o nome pra a direita
print('Que bom ter você aqui {:<20}!'.format(nome)) #Coloca o nome pra a esquerda
print('Que bom ter você aqui {:^20}!'.format(nome)) #Deixa o nome cetralizado
print('Que bom ter você aqui {:*^20}!'.format(nome)) #Deixa o nome cetralizado e com * nos espaços


n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))

so = n1 + n2
sub = n1 - n2
div = n1 / n2
div_int = n1 // n2
rest_div = n1 % n2
mu = n1 * n2
p = n1 ** n2

print('A soma dos números é {}, a subtração é {}, a divisão é {}, a multiplicação é {} , a divisão inteira é {}, o resto da divisão é {},'
      'a potência é {}'.format(so, sub, div, mu, div_int, rest_div, p ))

