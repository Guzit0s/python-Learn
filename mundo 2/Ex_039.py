
#Implora para o usuario digitar 6 numeros e soma somente os numeros pares, Afinal esse codigo é impofóbico e pratica odio ativo contra os numeros ímpares!


#Tentativa fracassada de tentar usar uma biblioteca para aprimorar o codigo
    #esc = ["N1: ",
    #    "N2: ",
    #    "N3: ",
    #    "N4: ",
    #    "N5: ",
    #    "N6: "]
    #ns = {}
    #for esc in esc:
    #    nums = int(input(esc))
    #    ns[esc] = nums
    #
    #N1 = ns[N1]
    #for ns[esc] in int:
    #    print(esc)

#Codigo nada haver kk
#a = input('digite um numero : ')
#b = input('Digite outro numero: ')
#
#for a in a :
#    a, b = int(a), int(b)
#    if a % 2 == 1 and b % 2 == 1:
#        print('é impar')
#    elif a % 2==1 and b % 2==0 or a % 2==0 and b % 2==1:
#        print('Cada um é um')
#    else:
#        print('é par')

                    ### IMPORTANTE! ###
#append, adiciona coisas a uma biblioteca, nesse caso ele adiciona os valores perguntados a suas respectivas casas
    #ex: N1 = 0 (isso dentro da lista), mas depois do append, o valor da casa 0 deixa de ser "N1" e vira o valor escrito pelo usuario!
print('Digite 6 numeros!\n')
esc = ["N1: ","N2: ","N3: ","N4: ","N5: ","N6: "]
num = []
tt = 0
for esc in esc:
    nums = int(input(esc))
    num.append(nums)
    if nums % 2 == 0 :
        tt += nums
print(f'\nA Soma de todos os numeros pares é {tt}')
