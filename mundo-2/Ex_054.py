#faz a mesma coisa que o 53 so que diferente

cont = 0
media = 0 

while True:
    n = int(input('\nQual Valor deseja adicionar?\n-> '))
    cnt = input('\nDeseja continuar?[S/N]\n-> ').upper()
    media += n
    cont += 1
    if cont == 1: #armazena o primeiro valor como o menor e maior, e depois trabalha em cima disso!
        maior = n
        menor = n 
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    if cnt == 'S':
        continue
    elif cnt == 'N':
        break

print(f'\nO Maior valor digitado é: {maior}\nJá o Menor valor: {menor}\n\nA media de todos os numeros digitados é: {media/cont}\n\nO codigo rodou {cont} vezes\n')

#Quando com paciencia, lembrar de arrumar o codigo, para quando o usuario digitar algo diferente de 'S ou N' na 8 linha!
