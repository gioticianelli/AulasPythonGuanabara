largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura * altura
tinta  = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))