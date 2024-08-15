#pede o peso de 5 pessoas, e diz quem ta mais gordo e quem ta menos!

#Precisei "copiar" a resposta, para entender a logica de manipulação atraves do primeiro valor!

maior = 0
menor = 0
for g in range(1,5+1):
    peso = float(input(f'Qual o peso da {g}º pessoas?\n-> '))
    if g == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'menor peso: {menor}\nMenor peso: {maior}')
