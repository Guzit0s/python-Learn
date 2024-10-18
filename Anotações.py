import os
def clean_screen():
    os.system('cls')

''' Aprendendo um pouco sobre como "printar" as coisas de uma  array '''


#como usar duas arrays como um banco de dados para fazer uma lista, como se fosse "produto - Preço"!
array = []
array_2 = []

clean_screen()
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

#COISA NOVA ↓↓↓
array.extend([a, b]) #adiciona os valores pedidos a lista!
#ultilizei "extend" para fazer com que adicionasse 2 itens de uma unica vez, ao inves de usar append e ficar escrevendo varias linhas!

c = int(input('Valor ao lado do primeiro: '))
d = int(input('Valor ao lado do Segundo: '))
array_2.extend([c, d])

        #COISA NOVA ↓↓↓
for item, item_2 in zip(array, array_2):
    print(item, item_2)

'''O que zip() faz:
Ele "alinha" os itens das duas listas:
Pega o primeiro item da array (1) e o primeiro item da array_2 (3) e os combina.
Depois, faz o mesmo com o segundo item da array (2) e o segundo item da array_2 (4).
ai da pra printar um valor ao lado do outro como se existisse uma coluna entre eles!'''
