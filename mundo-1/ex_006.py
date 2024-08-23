#60$ o dia 0.15 por km

d= int(input('por quantos dias pretende usar o carro: '))
km=float(input('quilometragem estimada por dia: '))

tt= (d*60)+(km*0.15)

print('O aluguel para o seguinte periodo de {} dias é de R${}.\ncontanto com um juros de 0,15 centantovos por quilometro, estimasse R${:.2f} centavos.\nTotalizando R${}'.format(d, d*60, km*0.15, tt))