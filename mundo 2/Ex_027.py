# "o meu é maior que o seu!"

n1 = float(input('Qual o primeiro numero: '))
n2 = float(input('Qual o segundo numero: '))

if n1>n2:
    print(f'{n1:.2f} sem duvidas é maior que {n2:.2f}!')
elif n2>n1:
    print(f'{n2:.2f} sem duvidas é maior que {n1:.2f}')
else:
    print('os dois numero são iguais!')