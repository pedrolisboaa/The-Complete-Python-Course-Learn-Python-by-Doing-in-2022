conjuntos = set(list(range(10)))
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 23, 54, 23, 90}

print(conjuntos)
print(conjunto2)

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}
set_three = set_one.intersection(set_two)

print(set_three)

teste = [
    {
        'nome': 'Pedro',
        'numeros': {1, 2, 3, 5, 6}
    },
    {
        'nome': 'Marcelo',
        'numeros': {2, 4, 5, 6, 7}
    }

]
