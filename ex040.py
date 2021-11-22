#040
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
    print('O aluno está REPROVADO')
elif 7 > media >= 5:
    print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
    print('O aluno está na RECUPARAÇÃO')
elif media >= 7:
    print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
    print('O aluno está APROVADO')