# outro codigo que vou ter que refazer! [so que com while kk]

#a1 = int(input('\nQual o valor primario da sua PA: '))
#r = int(input('Qual é a razão da sua PA: '))
#tt = a1
#a = 0
#for n in range(10):
#    a += 1
#    print(f'{a}º termo é: {tt}')
#    tt += r

from time import sleep

a = 0

while True:
    a1 = input('Qual o primeiro termo da sua PA?\n->')
    num_True = a1.isnumeric()
    if num_True is True:
        r = input('Qual a razão da sua PA?\n->')
        razao_True = r.isnumeric()
        if razao_True is True:
            tt = a1
            a1, r, tt = int(a1), int(r), int(tt)
            for n in range(10):
                a += 1
                print(f'{a}º termo é: {tt}')  # isso aqui é onde calcula a PA!
                tt += r
            rpt = input('\nDeseja calcular uma nova PA? [S/N]\n->').upper()
            if rpt == 'S':
                a = 0
                continue
            elif rpt == 'N':
                print('finalizando...')
                sleep(2)
                break
            else:
                a = 0
                print('DIGITE UM VALOR VALIDA!!!')
                rpt = input('Deseja calcular uma nova PA? [S/N]\n->')
                if rpt == 'S':
                    a = 0
                    continue
                elif rpt == 'N':
                    print('finalizando...')
                    sleep(2)
                    break
                else:
                    print('\nCansei de voce!\n')
                    break
        else:
            print('\nPor favor Digite um numero, sem letras!!\n')
            pass
    else:
        print('\nPor favor Digite um numero, sem letras!!\n')
        continue