#fincanciamento de um barraco, com valor da parcela nao pode exceder 30% do salario do usuario

vlr = float(input('Qual o valor da casa que pretende comprar: '))
tmp = int(input('Sera paga em quantos anos: ')) 
slr = float(input('Qual o valor do seu salario: '))

ano = tmp * 12
parcel = vlr / ano
trint = (30/100)*slr

if parcel < trint:
    print(f'Seu fincanciamento foi aprovado em {ano:.0f} parcelas de {parcel:.2f}')
else:
    print(f'Seu fincanciamento infelizmente nao foi aprovado')