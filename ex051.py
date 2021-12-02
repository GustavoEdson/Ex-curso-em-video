#051
print('='*20)
print('10 termos de uma PA')
print('='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo, razao):
    print(f'{c}', end=' ')
print(end='acabou')