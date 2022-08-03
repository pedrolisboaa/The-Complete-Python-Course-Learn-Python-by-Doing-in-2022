class Student:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        print(sum(self.notas) / len(self.notas))


if __name__ == '__main__':
    pedro = Student('pedro', [1, 2, 3, 4, 5])
    juliana = Student('juliana', [2, 3, 5, 8])

    print(pedro.nome)
    print(pedro.notas)

    print(juliana.nome)
    print(juliana.notas)

    pedro.media()
    juliana.media()
