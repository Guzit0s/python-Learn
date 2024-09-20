#eu vou refazer meu ultimo codigo ultilizando case e match pra ver se eu entendo o conceito disso!

#       codigo originial!

'''import os # operational system
def clean_screen():
    os.system('cls')

flag = True
man = 0
woman = 0
people = 0

clean_screen()
amount_people = int(input('\nQuantas pessoas deseja adicionar em sua lista?\n-> '))
for i in range(1, amount_people+1):
    sex = input(f'\nWhats the gender of the {i}º people?[(M)an / (W)oman ]\n-> ').upper().strip()
    age = int(input('How old is this people?\n-> '))
    if sex == 'M':
        man += 1
    elif sex == 'W' and age < 20:
        woman += 1 
    elif age > 18:
        people += 1 

print(f"\nhv {man} mans and {woman} woman younger than 20\nand {people} people's are older than 18!\n")'''

#       codigo Refeito!

import os # operational system
def clean_screen():
    n = os.name
    if n == 'nt': #nt se remete a windows
        os.system('cls')
    else: #se nao for nt é posix (Mac e Linux)
        os.system('clear')

people = 0
woman = 0
man = 0
people = 0
#pelo que eu entendi, essa case faz com que minha função tenha varias funções simuntaneamente

# esse ": str" define que minha função trabalha com strings, se eu trabalhasse com um int por exemplo daria erro!

def add(condiction: str):
    global flag
    global woman
    global man
    global people
    match condiction:
        case 'W':
            woman += 1
            return woman
        case 'M':
            man += 1
            return man
        case '+18':
            people +=1
            return people
        
clean_screen()
amount = int(input('Quantas pessoas deseja adicionar?\n-> '))
for i in range(1, amount+1):           
    clean_screen()
    sex = input(f'\nQual o sexo da {i}º pessoa?[(W)oman / (M)an]\n-> ').upper()
    age = int(input('\nQual a idade dessa pessoa?\n-> '))
    if sex == 'W' and age < 20:
        add('W')
    elif sex == 'M':
        add('M')
    if age > 18:
        add('+18')
clean_screen()
print(f'\nna sua lista tem:\n[{woman}] Mulheres com menos de 20 anos!\n[{man}] Homens adicionados a lista!\n[{people}] pessoas maiores de 18 anos!')