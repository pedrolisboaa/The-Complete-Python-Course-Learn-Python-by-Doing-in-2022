nome_idade = {
    'Pedro': 29,
    'Juliana': 25,
    'Olivia': 2
}

for idade in nome_idade.values():
    print(idade)

for nome in nome_idade.keys():
    print(nome)

for chave, valor in nome_idade.items():
    print(f'chave - {chave}| valor = {valor}')