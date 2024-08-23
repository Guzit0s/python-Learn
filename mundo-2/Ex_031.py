#copiei um codigo que é meu, e refiz ele com mais viadagem

r1 = float(input('qual a medida da primeira reta: '))
r2 = float(input('qual a medida da segunda reta: '))
r3 = float(input('qual a medida da terceira reta: '))

if r1 < r2+r3 and r3 < r1+r2 and r2 < r1+r3:
    print('Com esses valores, É POSSIVEL fazer um triangulo')
    if r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Triangulo esse do tipo Isósceles!')
    elif r1 != r2 != r3:
        print('Trinagulo esse do tipo Escaleno!')
    else:
        print('Triangulo esse do tipo Equilátero!')
else:
    print('Com esses valores, É IMPOSSIVEL fazer um trianglin')