#043
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = altura * altura
formula = peso / imc
if formula < 18.5: 
    print('Seu IMC é de {:.1f} você está abaixo do peso normal!'.format(formula)) 
elif formula >= 18.5 and formula <= 25: 
    print('Seu IMC é de {:.1f} você está no peso ideal Nice!'.format(formula)) 
elif formula >= 25 and formula <= 30: 
    print('Seu IMC é de {:.1f} você está com Sobrepeso, recomendo uma dieta'.format(formula))
elif formula >= 30 and formula <= 40:
    print('Seu IMC é de {:.1f} você está em Obesidade, recomendo ir ao medico!'.format(formula))
elif formula >= 40:
    print('Seu IMC é de {:.1f} você está em OBESIDADE MÓRBODA acima do peso'.format(formula))
