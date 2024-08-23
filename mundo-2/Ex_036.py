#Mostra so os numeros pares entre 1 e a quantidade que o usuario escolher!

n = int(input('Digite um valor para saber quantos pares tem: '))
for n in range(2, n+2, 2):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')