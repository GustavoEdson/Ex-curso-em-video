#028

from random import randint 
computador = randint(0, 5) #faz o pc "PENSAR"
from time import sleep

print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Em que numero eu pensei? '))  #jogador tenta adivinhar 
print('processando...')
sleep(2)

if computador == jogador:
    print('Parabéns você conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no numero {} não no {}'.format(computador, jogador))

