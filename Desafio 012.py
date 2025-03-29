preco = float(input('Digite o valor do produto: '))
desconto = preco - (preco * 5 / 100)
print('Hoje é seu dia de sorte!\n'
      'O produto que custava R${} agora está custando R${}\n'
      'Você teve 5% de desconto!'.format(preco, desconto))