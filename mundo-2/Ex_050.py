#vou refazer esse lixo usando while e bla bla bla, alguem realmente le isso?

#a1 = int(input('\nQual o valor primario da sua PA: '))
#r = int(input('Qual é a razão da sua PA: '))
#tt = a1
#a = 0
#for n in range(10):
#    a += 1
#    print(f'{a}º termo é: {tt}')
#    tt += r

a1 = int(input('\nQual o valor primario da sua PA: '))
r = int(input('Qual a razão da sua PA: '))
tt = a1
a = 0

while a < 10:
    a += 1
    print(f'o {a}º termo é: {tt}')
    tt += r