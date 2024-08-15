#esse é uma merda! deu ate gatilho.
import datetime

nasc = int(input('Qual ano você nasceu: '))
ano = datetime.datetime.now().year
idade = ano - nasc
if idade < 18:
    print(f'Infelizmente você ainda não pode se alistar, faltam {18 - idade} anos para você!')
elif idade > 18:
    print(f'Parece que você ja excedeu o prazo de alistamento amigo, voce ja tem {idade - 18} ano(s) de atraso!')
else:
    print(f'Parabens, voce ja tem {idade} Esta pronto para servir!')