'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

#esse foi com o while
n = int(input('Digite um número para ver sua fatorial: '))
c = n 
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 
print('{}'.format(f))

#esse foi com o larço for (desafio do professor)
from math import factorial
n = int(input('Digite um número para ver sua fatorial: '))
for n in range(n, n+1):
    print(f'o fatorial de {n} é {factorial(n)}', end='')