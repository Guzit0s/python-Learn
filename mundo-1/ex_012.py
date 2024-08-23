#Lê de 1 a 9999 e mostra oq caralhos é cada casa
#eu me estressei muito nesse exercicio e nao consegui fazer mas ta ai
# um numero dividido com divisao inteira (//) por sua casa decimal (centena, mileiro, etc) e ultilizando "% 10" ele mostra sua casa decimal!

#como eu ia saber disso meu Deus....

num = int(input('digite um numero de 1 a 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10 
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'As casas decimais do numero são:\n\nunidade: {uni}\n\ndezena: {dez}\n\ncentena: {cen}\n\nmilhar: {mil}\n')