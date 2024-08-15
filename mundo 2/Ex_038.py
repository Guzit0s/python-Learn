#Taubada melhorada!

#n = int(input('Qual o valor deseja saber a tabuada: '))
#print('=-'*49)
#print(f'TABUADA DO {n}\n'.center(84))
#for i in range(0, 10+1):
#     print(f'{n}x{i}: {n*i}'.center(84))
#print('=-'*49)

n = int(input('digite um numero: '))

def multiplo(x, y):
    return x * y
def printar_tabuada(x):
    for i in range(1,11):
        print(f'{i}x{x}: {multiplo(x, i)}')

printar_tabuada(n)
