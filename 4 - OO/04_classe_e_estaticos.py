class Estudante:
    def __init__(self, nome, escola):
        self.nome = nome
        self.escola = escola
        self.notas = []

    #@property
    def media(self):
        return sum(self.notas) / len(self.notas)


if __name__ == '__main__':
    pedro = Estudante('Pedro', 'UNB')
    pedro.notas.append(60)
    pedro.notas.append(66)
    pedro.notas.append(94)

    #print(pedro.media)
    print(pedro.media())

