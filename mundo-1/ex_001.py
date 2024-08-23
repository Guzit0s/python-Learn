#saber os dados de um caractere, se é numerico, alfabetico ou os dois!

ob=input('qual caractere gostaria de examinar?\n')
tp=type(ob)
num=ob.isnumeric()
al=ob.isalpha()
anum=ob.isalnum()
print('seu caractere foi {}\ntype: {}\nIs numeric: {}\nis alphabetic: {}\nis numeric or alphanetic: {}\n'.format(ob,tp,num,al,anum))