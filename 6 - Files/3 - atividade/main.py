from random import choice

perguntas = []
PONTOS = 0

with open('questoes.txt', 'r') as arquivo:
    todas_perguntas = arquivo.readlines()
    for i in range(10):
        pergunta = choice(todas_perguntas)
        perguntas.append(pergunta.replace('\n', ''))

for i in range(len(perguntas)):
    pergunta_utilizada = perguntas[i].split('=')
    resposta_jogador = input(f'Informe o resultado de {pergunta_utilizada[0]}: ')
    resposta_correta = pergunta_utilizada[1]

    if resposta_jogador == resposta_correta:
        PONTOS += 1
    else:
        with open('respostas.txt', 'a', encoding='utf-8') as resposta:
            resposta.write(
                f'Errou {pergunta_utilizada} o resultado é {resposta_correta} e você escreveu {resposta_jogador}\n')

print(f'Você acertou {PONTOS} de {len(perguntas)}')
with open('respostas.txt', 'r', encoding='utf-8') as final:
    for linha in final.readlines():
        print(linha)

