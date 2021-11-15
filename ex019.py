#019
'''programa que sorteia pessoas aleatorias UAU'''

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

ganhador = [n1, n2, n3, n4]

escolhido = random.choice(ganhador)
print('O ganhador foi {}'.format(escolhido))
