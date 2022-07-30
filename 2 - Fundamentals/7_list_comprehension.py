um_a_dez = list(range(10))
dobro = [x * 2 for x in um_a_dez]
um_ao_100 = list(range(1, 101))

nomes = ['Gregory Davis', 'Arthur Howard', 'Steven Harris', 'Kendra Solomon', 'Taylor Turner']
nomes_upper = [nome.upper() for nome in nomes]
pares = [x for x in um_ao_100 if x % 2 == 0]
impar = [x for x in um_ao_100 if x % 2 != 0]


print(dobro)
print(nomes_upper)
print(pares)
print(impar)