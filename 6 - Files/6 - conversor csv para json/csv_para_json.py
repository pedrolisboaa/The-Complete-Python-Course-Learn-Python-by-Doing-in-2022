import json

json_para_escrever = []

with open('arquivo.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    linha_completa = linha.strip().capitalize().split(',')

    time = linha_completa[0]
    cidade = linha_completa[1]
    pais = linha_completa[2]

    json_para_escrever.append(
        {
            'time': time,
            'cidade': cidade,
            'pais': pais
        }
    )

with open('arquivo.json', 'w') as arquivo_jason:
    json.dump(json_para_escrever, arquivo_jason, indent=6)
