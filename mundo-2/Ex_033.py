#escolheum produto e a maneira como vai ser pago

pdt = int(input('Qual produto deseja comprar?\n\n1 - Coquinha jelida R$500\n2 - Guardanapo semi novo R$300\n3 - shampo para curar mansidão de corno R$10.000\n\nEscolha um: '))

pgt = int(input('\nQual a forma de pagamento?\n\n1 - Money vivo\n2 - Debito\n3 - Credito (ate 2x sem juros)\n\nDigite sua escolha: '))

if pdt == 1:
    coca = 500
    if pgt == 1:
        print(f'Valor final com 10% de desconto: {coca-(10/100)*coca}')
    elif pgt == 2:
        print(f'Valor final com 5% de desconto no cartão de Debito: {500-(5/100)*500}')
    else:
        parcel = int(input('\nEm quantas vezes deseja parcelar sua compra (ate 2x sem juros): '))
        if parcel <= 2:
            print(f'{parcel} parcelas de: {coca / parcel}')
        else:
            juros = (20/100)*coca 
            print(f'{parcel} parcelas de: {(coca/parcel)+juros}')
elif pdt == 2:
    Grd = 300
    if pgt == 1:
        print(f'Valor final com 10% de desconto: {Grd-(10/100)*Grd}')
    elif pgt == 2:
        print(f'Valor final com 5% de desconto no cartão de Debito: {Grd-(5/100)*Grd}')
    else:
        parcel = int(input('\nEm quantas vezes deseja parcelar sua compra (ate 2x sem juros): '))
        if parcel <= 2:
            print(f'{parcel} parcelas de: {Grd / parcel}')
        else:
            juros = (20/100)*Grd 
            print(f'{parcel} parcelas de: {(Grd/parcel)+juros}')
else:
    shmp = 10000
    if pgt == 1:
        print(f'Valor final com 10% de desconto: {shmp-(10/100)*shmp}')
    elif pgt == 2:
        print(f'Valor final com 5% de desconto no cartão de Debito: {shmp-(5/100)*shmp}')
    else:
        parcel = int(input('\nEm quantas vezes deseja parcelar sua compra (ate 2x sem juros): '))
        if parcel <= 2:
            print(f'\n{parcel} parcelas de: {shmp / parcel}')
        else:
            juros = (20/100)*shmp 
            print(f'{parcel} parcelas de: {(shmp/parcel)+juros}')
    