import json

with open('arquivo.json', 'r') as arquivo:
    todo_arquivo = json.load(arquivo)

with open('teste.csv', 'a', encoding='utf-8') as arquivo_teste:
    for dado in todo_arquivo:
        time = dado['time']
        cidade = dado['cidade']
        pais = dado['pais']

        arquivo_teste.write(','.join([time, cidade, pais]))
        arquivo_teste.write('\n')
