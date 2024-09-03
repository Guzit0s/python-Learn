#Esse aplicativo é a primeira aula de "while"
#ou seja, exercicio bestinha

c = ''
sex = ''
m = 0
f = 0
while c != 'N':
    sex = input('Qual seu Genero?[M/F]: ').upper()
    if sex == 'M': 
        m += 1
    elif sex == 'F':
        f += 1
    else:
        print('Digite um genero valido!\n')

    #isso aqui foi uma melhor desnecessaria, mas eu fiz mesmo assim.↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    c = input('Deseja continuar?[S/N]: ').upper()
    if c != 'S' and c != 'N':
        print('Digite um valor valido!\n')
        c = input('Deseja continuar?[S/N]: ').upper()

print(f'Foram colocardos\n {m} homem(s)\ne {f} mulhere(s)!')