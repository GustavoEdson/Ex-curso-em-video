#ex064 
n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: ')) 
print(f'você digitou {cont} números e a soma é {soma}')