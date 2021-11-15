#ex022

nome = str(input('Qual é o seu nome? ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas fica {}'.format(nome.upper()))
print('Seu nome me minusculas fica {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))


'''print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))''' #primeira forma 

separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome[0], len(separa[0])))