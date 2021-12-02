#Exercício Python #056, Analisador completo
soma_idade = 0 
media_idade = 0
maior_de_homem = 0
nome_velho = ''
total_mulher = 0
for p in range(1, 5):
    print(f'------- {p} PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]'))
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_de_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_de_homem:
        maior_de_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1 
media_idade = soma_idade / 4 
print(f'A média de idade do grupo é {media_idade}')
print(f'O homen mais velho tem {maior_de_homem} e se chama {nome_velho}')
print(f'Ao todo são {total_mulher} mulheres com menos de 20 anos')