#transforma um numero em octal, binario ou hexadecimal

n = int(input('Escolha um numero qualquer: '))
form = int(input('Escolha a formatação de sua preferencia!\n1 - Binario\n2 - Octal\n3 - Hexadecimal\n\nSua escolha: '))

if form == 1:
    print(f'Em Binario seu numero é {bin(n)}!')
elif form == 2:
    print(f'em Octal seu numero é {oct(n)}!')
else:
    print(f'em Hexadecimal seu numero é {hex(n)}!')