#pede 3 numeros e me fala qual o maior e mais legal, e o menor e mais chato
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

#numero maior e mais legal
if n1<n2>n3 :
    print(f'\nSeu maior e mais legal numero é {n2}')

elif n2<n1>n3:
    print(f'\nSeu maior e mais legal numero é {n1}')

else:
    print(f'\nSeu maior e mais legal numero é {n3}')

#numero menor e mais chato
if n1>n2<n3 :
    print(f'\nJá seu menor e mais chato numero é {n2}')

elif n2>n1<n3:
    print(f'\nJá seu menor e mais chato numero é {n1}')

else:
    print(f'\nJá seu menor e mais chato numero é {n3}')