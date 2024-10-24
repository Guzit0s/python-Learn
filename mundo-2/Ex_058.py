#: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

import os

'''Manipuladores de tela'''

def clean_screan():
    name = os.name
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def skip():
    os.system('pause')

'''Funcões para validar inputs!''' 

def true_menu() -> int:
        while True:
            try:
                x = int(input('\nMenu inicial!\n\n[1] Adicionar itens\n[2] Ver itens no carrinho\n[3] Finalizar compra\n\n-> '))
                if x < 1 or x < 4:
                    return x
                else:
                    clean_screan()
                    print('\nDigite um valor valido!')
            except ValueError:
                clean_screan()
                print('\nDigite um valor valido!')

def true_value() -> float:
    while True:
        try:
            price = float(input('\nQual o valor do produto?\n-> '))
            if price >= 0:
                return price
            else:
                print('O numero nao pode ser negativo!\n')
        except ValueError:
            print('Digite um valor valido!\n')

'''Contadores'''

cheap = 1000
qnt = 1
tt = 0
cheap_name = ''
expensive = 0
flag = True

'''Uma especie de banco de dados para guardar os itens adiciodados!'''

shop_list = []
item_value = []

'''Fator logico'''

clean_screan()
print('\nBem vindo ao mercado Chato!')
while flag:
    menu = true_menu()

    # 1 - Adiciona item ao carrinho
    if menu == 1: 
        while True:
            item = str(input(f'\nQual o {qnt}º Produto de sua lista?\n-> '))
            value = true_value()

            shop_list.append(item) #Adiciona o item a lista para consulta
            item_value.append(value) #Adiciona o preço do item a lista para conquista

            if value < cheap:
                cheap = value
                cheap_name = item
            if value >= 1000:
                    expensive += 1

            tt += value
            qnt += 1

            add_item = str(input('\nDeseja adicionar mais algum item?[S/N]\n-> ')).strip().upper()
            if add_item == 'S':
                clean_screan()
                continue
            else:
                break
            
    # 2 - Consulta itens no carrinho lado a lado (produto e preço)
    elif menu == 2:
        clean_screan()
        print('\nSeus produtos são:\n')
        for item, value in zip(shop_list, item_value):
            print(f'{item} - R${value:.2f}')

    # 3 - Finaliza o codigo e entrega o resultado final
    else:
        break
print(f'\nnome do produto mais barato: {cheap_name}\nValor do protudo mais barato: {cheap}\nQuantidade de produtos que passam de R$1000: {expensive}\nTotal da compra: {tt}\n')
