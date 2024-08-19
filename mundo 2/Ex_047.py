#Refazendo codigo ultilizando while

'''num = int(input('digite um numero de 1 a 5: '))
num_pc = [1,2,3,4,5]
pc = random.choice(num_pc)
if num == pc:
    print(f' por algum motivo voce acertou, a maquina escolheu {pc} e voce tambem??????... BRUXO')
else:
    print(f'sua derrota ja era esperada, a maquina escolheu {pc}')'''

import random
tt = 1
n = 0
pc = random.randint(1,5)
while pc != n:
    n =  int(input('Digite um numero de 1 a 5!\n-> '))
    pc = random.randint(1,5)
    if pc == n:
        print(f'Voce precisou de {tt} tentativas para vencer!\nVoce escolheu {n} e a maquina {pc}')
        break
    else:
     tt += 1
     print(f'Tente novamente!\n o computador escolheu: {pc}!')
