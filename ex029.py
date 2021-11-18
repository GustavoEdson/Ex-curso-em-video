#ex029
velocidade = float(input('Qual é a velocidade atual do seu carro agora? ')) #perguntar a velocidade 
muta = (velocidade - 80) * 7
if velocidade > 80:
    print('voce vai receber uma multa de $RS{} por ultrapassar o limite de velocidade'.format(muta))
    
print('Voce está dirigindo em uma velocidade segura tenha um bom dia!')
