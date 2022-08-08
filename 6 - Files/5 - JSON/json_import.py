import json

# Lendo um arquivo JSON
with open('amigos.json', 'r', encoding='utf-8') as arquivo:
    # lê arquivos e transforma-los em dicionário
    conteudo = json.load(arquivo)

print(type(conteudo))
print(conteudo)

# Escrevendo um arquivo JSON

carros = [
    {"marca": "FIAT", "modelo": "Uno"},
    {"marca": "FORD", "modelo": "Fiesta"},
    {"marca": "AUDI", "modelo": "A3"}
]

with open('marca_de_carros.json', 'w') as arquivo:
    # chama o dump (nome da variavel com dicionario, arquivo onde ficara, e ident 6 para ficar bonito)
    json.dump(carros, arquivo, indent=6)

