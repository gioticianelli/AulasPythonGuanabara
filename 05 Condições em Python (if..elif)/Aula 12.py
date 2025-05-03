nome = str(input('Digite seu nome: '))
if nome == 'Romero':
    print('Seu nome é bonito!')
elif nome == 'pedro' or nome == 'Ana' or nome == 'Gabriel' or nome == 'Silva':
    print('Nome popular brasileiro')
else:
    print('Nome comum')
print('Prazer em te conhecer {}'.format(nome))