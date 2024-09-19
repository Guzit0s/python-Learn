# enunciado
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

import os # operational system
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

print(f"\nhv {man} mans and {woman} woman younger than 20\nand {people} people's are older than 18!\n")

#o codigo funciona e eu to com medo de mexer e ele parar de funcionar, entao é isso ai!
