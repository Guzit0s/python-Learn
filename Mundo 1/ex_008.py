#amaldiçoada seja a matematica e soma dos catetos

import math

c1= float(input('qual o valor do primeiro cateto: '))
c2= float(input('qual o valor do segundo cateto: '))

x = c1**2 + c2**2
c = math.sqrt(x)
print('{:.2f}'.format(c))