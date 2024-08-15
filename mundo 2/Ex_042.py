#palindromos!
#ultilizei o "replace" para tirar os espaços de dentro da frase
#Ex: "oi mano" com replace "oimano"

frs = input('Digite uma frase!\n-> ').upper().strip()
inv = frs[::-1]
frs = frs.replace(' ', '')
inv = inv.replace(' ','')
if frs == inv:
    print(f'"{frs}" Ao contrario fica "{inv}", então ela é uma frase Palindroma!')
else:
    print(f'"{frs}" Ao contrario fica "{inv}", então ela não é uma frase Palindrome!')
