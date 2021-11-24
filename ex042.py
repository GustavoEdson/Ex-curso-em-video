#042
print('-=-'*15)
print('Anaçisador de Triângulos')
print('-=-'*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r3 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um Triângulo', end=' ')
    if r1 + r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('ÉQUILÁTERO')
    elif r1 != r2 != r2 != r3 != r1:
        print('ECALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÂO PODEM formar triângulos')
