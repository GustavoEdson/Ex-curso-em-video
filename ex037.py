#ex037
num = int(input('Digite um numero inteiro: '))
print('''escolha um numero para a conversão de bases
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para EXIMADECIMAL''')

opção = int(input('Sua opção: '))
if opção == 1:
    print('{} foi convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} foi convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} foi convertido par EXIMADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção ivalida. Tente novamente')