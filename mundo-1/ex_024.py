#pega retas e faz um triangulo dentro do seu cu

r1 = float(input('qual a medida da primeira reta: '))
r2 = float(input('qual a medida da segunda reta: '))
r3 = float(input('qual a medida da terceira reta: '))

if r1 < r2+r3 and r3 < r1+r2 and r2 < r1+r3:
    print('Com esses valores, É POSSIVEL fazer um triangulo')
else:
    print('Com esses valores, É IMPOSSIVEL fazer um trianglin')
