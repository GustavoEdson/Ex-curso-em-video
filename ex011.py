#011
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

m = a*l
area = m / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}M².'.format(l,a,m))
print('Para pintar essa parede voce vai precisar de {}l de tinta.'.format(area))