def cem_numeros():
    x = 0
    while x < 100:
        yield x
        x += 1


teste = cem_numeros()

print(teste)
print(next(teste))
print(next(teste))
print(next(teste))
