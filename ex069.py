#ex069
cont = 0
homen = 0
mulher = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    idade = int(input('Idade: '))
    sexo = ' ' 
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('='*20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homen += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    if resposta == 'N':
        print(f'Temos {cont} pessoas com mais de 18 anos')
        print(f'Ao todos temos {homen} homens cadastrados.')
        print(f'E temos {mulher} mulheres com menos de 20 anos')
        break