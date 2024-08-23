#Contador de maior idade de 7 pessoas

from datetime import date
ano = date.today().year
jr = 0
cont = 0
for i in range(1,8):
    id = int(input(f'Digite o ano de nascimento da {i}º pessoa: '))
    if ano - id >= 18:
        cont += 1
    else:
        jr += 1
print(f'{cont} pessoas, já alcançaram a maior idade, e {jr} pessoas ainda nao são adultas!')
