#x018
import math 
angulo = float(input('Digite um angulo que voce deseja: '))

'''seno'''
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

'''Cosseno'''
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, seno))

'''Tangente'''
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))