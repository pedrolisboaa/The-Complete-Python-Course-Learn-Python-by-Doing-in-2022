class Estudante:
    def __init__(self, nome, escola):
        self.nome = nome
        self.escola = escola
        self.notas = []

    def media(self):
        return sum(self.notas) / len(self.notas)


class EstudanteTrabalho(Estudante):
    def __init__(self, nome, escola, salario):
        super().__init__(nome, escola)
        self.salario = salario

    @property
    def salario_mensal(self):
        return f'Salário R$ {self.salario * 44 * 4:.2f}'


pedro = EstudanteTrabalho('Pedro', 'UNB', 50)
juliana = Estudante('Juliana', 'UDF')

pedro.notas.append(60)
pedro.notas.append(70)
pedro.notas.append(80)

juliana.notas.append(80)
juliana.notas.append(90)
juliana.notas.append(99)


print(pedro.media())
print(pedro.salario_mensal)

print(juliana.media())

