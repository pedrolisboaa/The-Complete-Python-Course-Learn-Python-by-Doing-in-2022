filmes = [
    {
        'titulo': 'Harry Potter',
        'genero': 'Fantasia',
        'ano_lancamento': '2000'
    },
    {
        'titulo': 'Matrix',
        'genero': 'ação',
        'ano_lancamento': '1996'
    },
    {
        'titulo': 'vingadores',
        'genero': 'aventura',
        'ano_lancamento': '2015'
    },

]

somente_titulos = {t['titulo']: t for t in filmes}

print(somente_titulos)
