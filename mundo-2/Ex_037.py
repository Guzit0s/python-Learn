#Mostra qual a soma de todos os numeros impares no intervalo de 1 e 500, o motivo? nao sei! kkkk

#Ultilizar '+=' é incrivel! 
#Voce pode colocar qualquer operação matematica no lugar do '+' e simplificar o codigo!!!!!!!

tt = 0
for n in range(0, 500+1):
    if n % 3 == 0 and n % 2 == 1:
      tt += n 
print(f'O resultado da soma de todos os numeros impáres e divisiveis por 3 no intervalo de 1 e 500 é {tt}')
