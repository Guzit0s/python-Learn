#le o primeriro e ultimo nome separadamente

nm = str(input('qual seu nome completo: ')).strip()
first_nm = nm.split()
last_nm = nm.rsplit()
print(f'seu primeiro nome é {first_nm[0]} ja seu ultimo nome é {last_nm[-1]}')