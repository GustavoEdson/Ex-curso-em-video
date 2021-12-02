#059 
from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
n = 0
while n == 0:
    print('''
    ======================
    [ 1 ] Somar 
    [ 2 ] Multiplicar 
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] sair do programa
    ======================''')
    tipo = int(input('Escolha um tipo: '))
    print('Carregando...')
    sleep(1)
    if tipo == 1:
        print(f'{primeiro_valor} + {segundo_valor} é {primeiro_valor+segundo_valor}.', end=' ')
    if tipo == 2:
        print(f'{primeiro_valor} x {segundo_valor} é {primeiro_valor*segundo_valor}.', end=' ')
    if tipo == 3:
        if primeiro_valor > segundo_valor:
            print(f'{primeiro_valor} é maior que {segundo_valor}.', end=' ')
        elif primeiro_valor == segundo_valor:
            print(f'{primeiro_valor} e {segundo_valor} são iguais!', end=' ')
        else:
            print(f'{segundo_valor} é maior que {primeiro_valor}.', end=' ')
    if tipo == 4:
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
    if tipo > 5:
        print('Opção invalida! tente novamente.', end=' ')
    if tipo == 5:
        n = 5
print('Você saiu do prgrama!')