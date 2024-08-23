#adivinhar o numero que meu pc pensou... se é que ele pensa
import random

num = int(input('digite um numero de 1 a 5: '))
num_pc = [1,2,3,4,5]
pc = random.choice(num_pc)
if num == pc:
    print(f' por algum motivo voce acertou, a maquina escolheu {pc} e voce tambem??????... BRUXO')
else:
    print(f'sua derrota ja era esperada, a maquina escolheu {pc}')
