#vou refazer esse lixo usando while e bla bla bla, alguem realmente le isso?

#a1 = int(input('\nQual o valor primario da sua PA: '))
#r = int(input('Qual é a razão da sua PA: '))
#tt = a1
#a = 0
#for n in range(10):
#    a += 1
#    print(f'{a}º termo é: {tt}')
#    tt += r

a1 = 0
r = 0
a = 0
t = 0

while True:
    a1 = int(input('\nDigite o valor primario da sua PA [ou 0 para sair]: '))
    tt = a1
    if a1 > 1:
        r = int(input('Qual a razão da sua PA: '))
        t = int(input('Quantos termos deseja?\n-> '))
        for i in range(0, t):
            a += 1
            print(f'o {a}º termo é: {tt}')
            tt += r
        c = input('\nDeseja continuar?\n[S/N]: ').upper()
        if c == 'S':
            a = 0
            continue
        else:
            print('\nAcabou')
            break
    else:
        print('finalizando...')
        break