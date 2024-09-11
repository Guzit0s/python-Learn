#impar ou par com seu pc, afinal, voce so tem ele, voce é sozinho, Lide com isso hahahah!

import os
import random
vitorias = 0
flag = True

def limpa_tela():
    os.system('cls')

while flag:
    limpa_tela()
    pc = random.randint(0,10)
    chose = int(input('Qual sua escolha?\n\n[1] Impar\n[2] par\n\n-> '))
    if chose > 2:
        while chose != 1 and chose != 2:
            print('Digite um valor valido!\n')
            chose = int(input('Qual sua escolha?\n\n[1] Impar\n[2] par\n\n-> '))
    num = int(input('Qual sua jogada?\n-> '))
    soma = pc + num

    #usuario [impar ou par] ganha
    if  chose == 1 and soma % 2 == 1 or chose == 2 and soma % 2 == 0:
        vitorias += 1
        print('Você ganhou\nVamos para a proxima rodada!\n')
        os.system('pause') #"aprete qualquer tecla para continuar!" (isso é mto foda!)
        limpa_tela() #limpa o terminal!

    #usuario [impar ou par] perde
    else:
        cont = input(f'\nVocê Perdeu!\no computador escolheu {pc}\nSuas vitorias foram {vitorias}\n\nDeseja continuar?[S/N]\n-> ').upper().strip()
        if cont == 'S': 
            limpa_tela()
            
        elif cont == 'N':
            limpa_tela()
            flag = False
        else:
            #loop para saber se o usuario deseja tentar novamente!
            while cont != 'S' and cont != 'N':
                print('\nDigite um valor valido!!!\n')
                cont = input('Deseja continuar?[S/N]\n-> ').upper().strip()
                limpa_tela()
            if cont == 'N':
                flag = False
            
        
