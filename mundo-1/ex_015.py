# Saber quantas vezes aparece o 'a' na frase, qual a primeira posição e qual a urtima

frs = input('digite uma frase: ').strip()
frs = frs.lower()
vzs_a = frs.count('a')
prim_a = frs.find('a' +1)
ultm_a = frs.rfind('a'+1)
print(f'Sua frase tem {vzs_a} "a" , sendo o primeiro na casa {prim_a} e o ultimo na casa {ultm_a}')