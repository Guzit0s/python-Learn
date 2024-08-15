#sorteio

# variavel.split server para armazenar as respostas nas variaveis 

import random

aluns = input('nome dos alunos separado por virgula: ')
a1, a2, a3, a4 = aluns.split(',')
nomes = [a1,a2,a3,a4]

print(random.choice(nomes))

#caso queira ver a ordem embaralhada dos alunos use shuffle

# random.shuffle(nomes)
# print(nomes)