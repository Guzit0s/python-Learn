#programa de radar pra dar multa em mlk que mosca

s = int(input('Qual era sua velocidade: '))
if s >= 80:
    v = (s-80)*7
    print(f'voce foi multado o limite é 80km, o valor da sua multa sera de R${v}')
else:
    print('Sua avo pilota mais rapido e não toma multa! \n otario hahaha')