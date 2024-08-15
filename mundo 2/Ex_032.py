#Codigo pra saber se voce é digno do apelido Gordao!

alt = float(input('Qual sua altura: '))
pes = float(input('Qual seu peso atual: '))
imc = pes / alt**2
if imc <= 18.5:
    print(f'Seu IMC é de {imc:.2f}\nSai pra la magricela kkkk')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}\nSem novidades ate então.')
elif imc <= 30:
    print(f'com o IMC de {imc:.2f}\nvoce esta trilhando o caminho da obesidade...')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}\nFalta pouco para se tornar digno, por enquanto você so ta gordo mesmo kkkkk')
else: 
    print(f'IMC: {imc:.2f}\nInfelizmente você é digno do apelido gordão, parabens pelas suas veias entupidas KKKKK')