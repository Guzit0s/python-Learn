#Nome completo em maiusculo, minusculo, qnt de letras e qnt de letras do primeiro nome

nome = input('digite seu nome completo: ')
mai = nome.upper()
min = nome.lower()
qnt_nome1 = len(nome.split()[0])
spit = nome.split()
qnt_nome = len(''.join(spit))

print(f'Seu nome inteiro é {nome}\n\nem maiusculo é {mai}\n\nem minusculo é {min}\n\nseu nome tem {qnt_nome} letras\n\ne seu primeiro nome tem {qnt_nome1} letras!')