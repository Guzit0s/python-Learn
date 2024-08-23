#Faz um menuzinho meia boca pra uma calculadora feita na coxa

n1 = float(input('Qual o primeiro valor?\n-> '))
n2 = float(input('Qual o segundo valor?\n-> '))
r = 0
while r != 5:
    r = int(input('Oque deseja fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Numeros\n[5] Finalizar\n\n-> '))
    if r in range(0,6):   
        if r == 1:
            print(f'\nA soma de {n1} + {n2} = {n1+n2}\n')

        if r == 2:
            print(f'\nMultiplicando {n1} x {n2} temos {n1*n2}\n')
            
        if r == 3:
            if n1 > n2:
                print(f'\nO maior Numero entre {n1} e {n2} é {n1}!\n')
            elif n2 > n1:
                print(f'\nO maior Numero entre {n1} e {n2} é {n2}!\n')
            else:
                print('\nOs dois numero sao iguais!\n')
            
        if r == 4:
            n1 = float(input('\nQual o novo valor do primeiro numero?\n-> '))
            n2 = float(input('\nQual o novo valor do segundo numero?\n-> '))
            print('Numeros salvos!\n')
            
        if r == 5:
            print('finalizando...')
            break
    else:
        print('Digite um valor valido!\n')
        continue
