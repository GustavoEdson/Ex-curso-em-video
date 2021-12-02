#ex054
from datetime import date
maior = 0
menor = 0 
atual = date.today().year
for pessoas in range(1, 8):
    idade = int(input('Qual é idade da {} pessoa: '.format(pessoas)))
    soma = atual - idade   
    if idade >= 18:
        maior +=1
    if idade <= 18:
        menor += 1
print(f'temos {maior} de maior de idade')
print(f'e também temos {menor} menor de idade')