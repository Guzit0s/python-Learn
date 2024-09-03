#oq é uma sequencia de fibonacci????? e pra que serve essa merda kkkk

n = int(input('Quantos numeros deseja ver na sequencia de fibonacci?\n-> '))
n1 = 0
n2 = 1
passo = 0
while passo < n:
    print(n1, end = '  ')
    soma = n1 + n2
    n1 = n2
    n2 = soma
    passo += 1
