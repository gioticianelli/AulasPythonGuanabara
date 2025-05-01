frase = 'Bolo de Cenoura com Chocolate'


print('Bolo de Cenoura com Chocolate\n')

# Fatiamento
print('-----FATIAMENTO-----')
print(frase[2:11])
print('-----------------\n')

# Análise
print('-----ANÁLISE-----')
print(frase.find('Chocolate'))
print(frase.count('o'))
print('-----------------\n')

# Transformação
print('-----TRANSFORMAÇÃO-----')
print(frase.replace('Chocolate', 'Calda de chocolate'))
print(frase.capitalize())
print(frase.title())
print(frase.rstrip())
print(frase.lstrip())
print(frase.upper())
print(frase.lower())
print('-----------------\n')

# Divisão
print('-----DIVISÃO-----')
print(frase.split())
print('-----------------\n')

# Junção
print('-----JUNÇÃO-----')
print('!'.join(frase.split()))
print('-----------------')

