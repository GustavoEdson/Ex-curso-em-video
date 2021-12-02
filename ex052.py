#052
numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO numero {} foi divísivel {} vezes'.format(numero, tot))
if tot == 2:
    print('Esse numero é primo')
else:
    print('Esse numero não é primo!')