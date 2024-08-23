#Categoriza voce pela sua idade!

import datetime

ano = datetime.datetime.now().year
nas = int(input('Qual Ano você nasceu: '))
id = ano - nas

if id <= 9:
    print(f'Com a idade de {id} anos, sua categoria é MIRIM!')
elif id <= 14:
    print(f'Com a idade de {id} anos, sua categoria é INFANTIL!')
elif id <= 19:
    print(f'Com a idade de {id} anos, sua categoria é JUNIOR!')
elif id <= 20:
    print(f'Com a idade de {id} anos, sua categoria é SÊNIOR!')
else:
    print(f'Com a idade de {id} anos, sua categoria é MASTER!')