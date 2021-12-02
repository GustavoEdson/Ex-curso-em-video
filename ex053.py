#ex053
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
# inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('o inverso da {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')