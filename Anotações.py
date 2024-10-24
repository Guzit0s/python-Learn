import os
def clean_screen():
    os.system('cls')

menu = int(input('Menu de Aprendizado, qual exemplo deseja ver?\n[1] Exemplo Array!\n[2] Exemplo Try!\n[3] em breve...\n\n-> '))

if menu == 1:
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

elif menu == 2:
    ''' Um pouco sobre try e except! '''

    #aqui tem um exemplo simples de como try é ultilizado para a validação de inputs, isso é muito bom!
    #podemos ver tambem que Try nao funciona sem um except, nesse caso eles sao tipo umm "if esle" ou "match case"
    #se o codigo dentro do try quebrar ele redireciona imediatamente para o codigo do except, assim o programa nao quebra!

    try:
        x = int(input('Digite um numero: ')) 
        print(f'o numero que voce digitou é {x}')
    except:
        print('Isso nao é um numero!')

else:
    print('Essa opção nao esta disponivel!\n')

