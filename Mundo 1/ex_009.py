#seno cosseno e a desgraça toda

import math

a = int(input('qual o angulo da sua imagem: '))
rad = math.radians(a)
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)

print('seno: {:.2f}\ncos: {:.2f}\ntan: {:.2f}'.format(sen,cos,tan))