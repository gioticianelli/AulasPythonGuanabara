#Condição simples
'''name = str(input('Qual seu nome? '))
if name == 'Robson':
    print('Que nome bonito!')
else:
    print('Seu nome é feio!')
print('Bom dia, {}!'.format(name))'''


#Condição composta
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
n3 = float(input('Digite a 3° nota: '))
m = (n1 + n2 + n3) / 3
if m >= 6:
    print('Parbéns você passou de ano!')
else:
    print('Você ficou de recuperação.')
print('Sua média foi de {:.2f}'.format(m))



