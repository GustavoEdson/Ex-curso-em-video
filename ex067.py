#ex067
while True:
    print('-'*32)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*32)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Programa da tabuada encerrado volte sempre!')