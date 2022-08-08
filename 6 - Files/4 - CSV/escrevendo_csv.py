with open('dados.csv', 'r') as arquivo:
    tudo = arquivo.readlines()

for linha in tudo[1:]:
    dados = linha.strip().split(',')
    nome = dados[0].title()
    idade = dados[1]
    faculdade = dados[2].upper()
    curso = dados[3].capitalize()

    print(f'{nome} possui {idade} anos, estudou na {faculdade} e fez o curso de {curso}.')


simples_csv = ','.join(['marcelo', '36', 'ceub', 'direito'])
with open('dados.csv', 'a') as arquivo:
    arquivo.write(simples_csv)


