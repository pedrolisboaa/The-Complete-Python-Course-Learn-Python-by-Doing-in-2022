esta_funcionado = True

while esta_funcionado:
    numero = input('Digite um número: ')
    try:
        numero = float(numero)
    except ValueError:
        esta_funcionado = False
        print(f'{numero} não é um número.')
    else:
        print(f'{numero} é um número.')

