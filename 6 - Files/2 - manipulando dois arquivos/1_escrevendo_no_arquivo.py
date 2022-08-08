# Escrevendo no arquivo
print(f'Vamos digitar o nome a cidade que 5 amigos moram.')
for _ in range(5):
    nome = input('Informe o nome do seu amigo: ')
    cidade = input('Informe a cidade que ele mora: ')

    with open('nomes_e_cidade.txt', 'a') as arquivo:
        arquivo.write(f'{nome} mora em {cidade}.\n')



