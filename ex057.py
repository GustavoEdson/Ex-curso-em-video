#057
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos tente novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')