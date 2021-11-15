#ex008

medida = int(input('digite um metro: '))

cm = medida * 100
mm = medida * 1000

print('a medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))