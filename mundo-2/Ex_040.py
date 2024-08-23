#fazer uma fucking PA!

a1 = int(input('\nQual o valor primario da sua PA: '))
r = int(input('Qual é a razão da sua PA: '))
tt = a1
a = 0
for n in range(10):
    a += 1
    print(f'{a}º termo é: {tt}')
    tt += r
