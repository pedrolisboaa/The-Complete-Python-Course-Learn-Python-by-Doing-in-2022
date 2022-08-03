# with open('dados.txt', 'r') as file:
#     print(file.read())
#
#
# with open('dados.txt', 'a', encoding='utf-8') as file:
#     file.write('Pedro')
#     file.write('\nPedrão')
#
#
# with open('dados.txt', 'r') as file:
#     print(file.read())

with open('nomes.txt', 'a') as file:
    nome = input('Informe seu nome: ')
    file.write(nome)