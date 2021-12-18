#ex066
n = cont = soma = 0
while True:
    n = int(input('Digite un número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores foi {soma}.')