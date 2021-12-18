#ex068
from time import sleep, time
from random import randint
vitorias = 0 
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*15)
    valor = int(input('Digite um valor: '))
    computador = randint(0, 10)
    jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if jogador == 'P':
        resultado = valor + computador
        print('Carregando...')
        sleep(1)
        print(f'Você jogou {valor} e o computador {computador}. Total deu {resultado}')
        if resultado % 2 == 1:
            print(f'GAMER OVER! você venceu {vitorias} vezes.')
            break
        else:
            if resultado % 2 == 0:
                print(f'Você venceu vamos jogar novamente....')
                vitorias += 1
    elif jogador == 'I':
            resultado = valor + computador
            print('Carregando...')
            sleep(1)
            print(f'Você jogou {valor} e o computador {computador}. Total deu {resultado}')
            if resultado % 2 == 0:
                print(f'GAMER OVER! você venceu {vitorias} vezes')
                break
            else:
                if resultado % 2 == 1:
                    print('Você venceu vamos jogar novamente...')
                    vitorias += 1