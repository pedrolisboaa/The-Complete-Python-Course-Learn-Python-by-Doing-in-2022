numeros = list(range(10))
nomes = ['David Sandoval', 'Tammy Montoya', 'George Reynolds', 'Tiffany Alvarez', 'Jason Reeves MD',
         'Thomas Patterson', 'Sarah Smith', 'Kayla Munoz', 'Jon Benson', 'Sarah Cooper']

numeros_nomes = zip(numeros, nomes)
for _ in numeros_nomes:
    print(_)