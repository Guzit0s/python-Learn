# mostra a tabuada do numero que voce pede, porem de uma maneira desnecessariamente complicada!

#faz a tabuada escolhida (porra, o nome é intuitivo ne mano kkkkk)
def imprime_tabuada(x):
    for i in range(1, multiplo_atual+1):
        print(f'{numero_atual} x {i} = {numero_atual * i}')

#Sistema de Armazenagem de resposta vinda do usuario
qnt = int(input('\nQuantas tabuadas deseja ver? (O programa sera finalizado, caso o numero de alguma das taboadas for negativo!)\n-> '))
tabuadas = []
multiplos = []
for posição in range(1, qnt+1):
    tb =  int(input(f'\nQual numero voce deseja ver a {posição}º tabuada? \n-> '))
    if tb > 0:
        tabuadas.append(tb)
    else:
        print('\nNumeros negativos, não serão aceitos!, até mais otario!\n')
        break
    n = int(input(f'\nAté qual valor deseja ver a Tabuada do {tb}?\n-> '))
    multiplos.append(n)

#condição de passo dentro da array e tambem o return da tabuada do numero recebido pelo usuario!
indice_tabuada = 0
indice_multiplos = 0
cont = 0
if tb > 0:
    while indice_tabuada < len(tabuadas): 
        numero_atual = tabuadas[indice_tabuada]
        multiplo_atual = multiplos[indice_multiplos]
        imprime_tabuada(numero_atual)
        indice_tabuada += 1
        indice_multiplos +=1
        cont += 1
else:
    print('Finalizando...')
