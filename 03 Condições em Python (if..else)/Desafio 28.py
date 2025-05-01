from random import randint
from time import sleep
comp = randint (0,5)  #Faz com que o computador sorte um número aleatório entre 0 e 5
print(50 * '-')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(50 * '-')
num = int(input('Qual número eu pensei?? '))
print('PROCESSANDO...')
sleep(2) # da um tempo até seguir para a próxima linha
if num == comp:
    print('PARABÉNS! Você conseguiu adivinhar')
else:
    print('GANHEI! Eu pensie no número 1 e não no {}'.format(num))

