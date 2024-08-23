#Saber se tem Silva no nome, se vc tiver, voce é pobre.
s= input('digite seu nome completo: ')
title = s.title()
silva = 'Silva' in title

if silva == True:
    print('Parabens pobre, voce é da familia silva')
else:
    print('foi por pouco amigo!')