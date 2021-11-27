# programa de contagem regressiva
from time import sleep
a = int(input('Escolha um numero: '))
for c in range(a, -1, -1):
    print('Restam {}!'.format(c))
    sleep(1)
print('\033[1;31mFeliz ano novo!!!')