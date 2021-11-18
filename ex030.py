#030 

numero = int(input('Me diga qualquer numero: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))