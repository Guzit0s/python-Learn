#Le varios numeros, se digitar 999 o programa morre e depois sai somando toda essa merda

numeros = [] # lembrar nome, array
tt = 0 
while True:
    a = int(input('\nDigite um numero\n-> '))
    if a != 999:
        numeros.append(a)
        tt += a
        continue
    else:
        break

print(f'\nVoce digitou {len(numeros)} numeros, e a soma deles deu: {tt}\n')