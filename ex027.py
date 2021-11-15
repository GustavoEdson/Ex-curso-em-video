#ex027

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('muito pra')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu segundo nome é {}'.format(nome[len(nome)-1]))