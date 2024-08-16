#Lê o nome, o sexo e a idade de 4 pessoas!

nm = ''
velho = -1
media_id = 0
velha = 0
for i in range(1,5):
    nome = str(input(f'\n\nQual o nome da {i}º pessoa?\n-> '))
    idade = int(input(f'Qual a idade da {i}º Pessoa?\n-> '))
    sex = input(f'Qual o sexo da {i}º pessoa? (H/M)\n-> ').upper()
    if sex == 'H': # mede o homem mais velho
        if idade > velho: 
            velho = idade
            nm = nome
    media_id += idade
    if sex == 'M':
        if idade >= 20:
            velha += 1


print(f'O nome do homem mais velho ->{nm}\nCom a idade de ->{velho}\nA media de idade dessas pessoas é: {media_id/i}\ne existem {velha} mulhere(s) com mais de 20 anos!')