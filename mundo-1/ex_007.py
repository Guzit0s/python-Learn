#mostra o numero inteiro de um numero quebrado, usando trunc
import math

n = float(input('digite um numero (quebrado de perferencia): '))
i = math.trunc(n)

print('o numero escolhido foi {}, o numero inteiro do mesmo é: {}'.format(n,i))