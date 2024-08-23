#aumento de salario, se salario for maior que R$1250,00 o aumento é de 10% se for menor ou igual o aumento é de incriveis 15%

s = float(input('Qual o seu salario atual?\nR: '))
if s <= 1250:
    print(f'\nVoce ganhou 15% de aumento salarial!\nSeu aumento sera de {(15/100)*s:.2f}\nTotalizando um salario de R${(15/100)*s+s:.2f} ')
else:
    print(f'Voce ganhou 10% de aumento salarial!\nSeu aumento sera de {(10/100)*s:.2f}\nTotalizando um salario de R${(10/100)*s+s:.2f}')