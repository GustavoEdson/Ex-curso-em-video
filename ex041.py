#041
from datetime import date #bliblioteca datetime
from time import sleep #bliblioteca time
atual = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
data = atual - nascimento
print('ANALISANDO...')
sleep(3)
print(f'O atleta tem {data} anos')
if data <= 9:
    print('Classifição MIRIM.')
elif data <= 14:
    print('Classifição INFANTIL.')
elif data <= 19:
    print('Classifição JÚNIOR.')
elif data <= 25:
    print('Classifição SÊNIOR.')
else:
    print('Classifição MASTER.')