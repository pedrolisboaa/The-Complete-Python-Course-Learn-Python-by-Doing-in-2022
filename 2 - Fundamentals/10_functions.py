def diga_oi():
    print('oi')


def return_ola():
    return 'ola'


def somar_dois(x, y):
    return x + y


def somar_varios(*args):
    return sum(x for x in args)


teste = somar_varios(1, 2, 3, 4, 5, 6)
print(teste)

x = 5
y = 6

print(lambda x, y: x + y)
