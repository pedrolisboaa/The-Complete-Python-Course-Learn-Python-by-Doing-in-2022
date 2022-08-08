from random import randint


def tabuada_multiplicacao():
    numero1 = randint(0, 99)
    numero2 = randint(0, 99)
    return f'{numero1}*{numero2}={numero1 * numero2}'


def tabuada_adicao():
    numero1 = randint(0, 99)
    numero2 = randint(0, 99)
    return f'{numero1}+{numero2}={numero1 + numero2}'


def tabuada_subtracao():
    numero1 = randint(0, 99)
    numero2 = randint(0, 99)
    return f'{numero1}-{numero2}={numero1 - numero2}'


def tabuada_divisao():
    numero1 = randint(0, 99)
    numero2 = randint(1, 99)
    return f'{numero1}/{numero2}={(numero1 / numero2):.2f}'


with open('questoes.txt', 'a') as arquivo:
    for i in range(100):
        arquivo.write(f'{tabuada_adicao()}\n')
        arquivo.write(f'{tabuada_subtracao()}\n')
        arquivo.write(f'{tabuada_multiplicacao()}\n')
        arquivo.write(f'{tabuada_divisao()}\n')

