#033
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando o quem é menor 
menor = a
if b < a and b < c:
    menor = a
if c < a and c < b:
    menor = c 
# Verificando quem é maior 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))