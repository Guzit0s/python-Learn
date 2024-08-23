#faz um fatorial de um numero
#eu pedi ajuda ao chat, e entendi a logica, mas nao 100% :(

f = 1 # começa com 1 pq o fatorial de 0 é 1

n = int(input('Qual o numero que voce quer fatorar?\n-> '))

print(f'{n}! = ', end='') # isso serve literalmente para aparecer "n! = " no inicio do codigo por puro charme

for i in range(n, 1, -1): # aqui o loop termina em 2 porque ja é a resposta final
    f *= i
    print(i, end='*')
    
print(f'1 = {f}') # o numero 1 é colocado de forma fixa para "embelezar" o codigo ja que no 2 ja temos a resposta!
    