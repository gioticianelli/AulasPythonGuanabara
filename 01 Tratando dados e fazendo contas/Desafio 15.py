dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preco = (60 * dias) + (0.15 * km)

print('O total a pagar pelo aluguel é de: {} '.format(preco))