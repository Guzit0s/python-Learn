#Ja fiz esse varias vezes, to ate cansado dele

n1 = float(input('Digite sua nota de alegria: '))
n2 = float(input('Digite sua nota de tristeza: '))

med = (n1+n2)/2

if med < 5.0:
    print('Banido com', med)
elif med > 7.0:
    print('Passou com', med)
else: 
    print('Recuperação com', med)