#jogo jokenpo!
from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: #computador escolheu PEDRA 
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('JOGADOR VENDCEU!')     
    else:
        print('JOGADA INVALIDA!')       
elif computador == 1: #computador escolheu PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')  
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #computador escolheu TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')   
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')