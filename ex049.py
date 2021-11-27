#049
print('''Tipos disponíveis!
[ 1 ] + 
[ 2 ] - 
[ 3 ] x 
[ 4 ] ÷ ''')
tipo = int(input('Escolha um tipo: '))
num = int(input('Digite um numero pra ver sua tabuada: '))
for c in range(1, 11):
    if tipo == 1:
        print(f'{num} + {c} = {num+c}')
    elif tipo == 2:
        print(f'{c} - {num} = {c-num}')
    elif tipo == 3:
        print(f'{num} x {c} = {num*c}')
    elif tipo == 4:
        print(f'{c} ÷ {num} = {c/num}')
if tipo > 4:
    print('Opção invalida!')