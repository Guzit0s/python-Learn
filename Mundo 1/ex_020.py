# esse é besta
#paga 0,50 centavos por km em ate 200km, caso for mais paga so 45 centavos

km = int(input('quantos kms tem sua viagem: '))

if km <= 200:
    print(f'sua passagem fica no valor de {km*0.50}')
else:
    print(f'voce ganhou um BAITA DESCONTO DE 5 CENTAVOS\nSendo assim, sua passagem pra casa do caralho fica {km*0.45}')
