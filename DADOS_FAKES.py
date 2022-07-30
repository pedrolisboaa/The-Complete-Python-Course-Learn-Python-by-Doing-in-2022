from faker import Faker

faker = Faker()


def gerar_lista_de_nomes():
    lista = []
    for i in range(10):
        lista.append(faker.name())
    print(lista)


gerar_lista_de_nomes()