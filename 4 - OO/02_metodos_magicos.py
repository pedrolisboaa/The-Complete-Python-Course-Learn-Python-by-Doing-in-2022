class Garagem:
    def __init__(self):
        self.carros = []

    def __len__(self):
        return len(self.carros)

    def __getitem__(self, item):
        return self.carros[item]

    def __repr__(self):
        return f'Garagem do pedrão!'


if __name__ == '__main__':

    minha_garagem = Garagem()
    print(minha_garagem.carros)
    minha_garagem.carros.append('Fusca')
    minha_garagem.carros.append('Monza')
    minha_garagem.carros.append('Clio')

    print(Garagem())
    print(minha_garagem)

    print(minha_garagem.carros)
    print(len(minha_garagem.carros))
    print(len(minha_garagem))
    print(minha_garagem[0])