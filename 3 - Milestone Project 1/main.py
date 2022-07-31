filmes = []

MENU = ('Informo o que deseja fazer:\n"a" adicionar um filme:\n"m" mostrar todos os filmes:'
        '\n"b" buscar um filme\n"s" sair do programa:\n ').lower()

iniciar_aplicacao = input(MENU)

while iniciar_aplicacao != 's':

    if iniciar_aplicacao == 'a':
        titulo = input('Informe o título do filme: ')
        diretor = input(f'Quem é o direito de {titulo}: ')
        ano_de_lancamento = input(f'Informe o ano de lançamento de {titulo}: ')

        filmes.append({
            'titulo': titulo,
            'diretor': diretor,
            'ano_lancamento': ano_de_lancamento
        })

    elif iniciar_aplicacao == 'm':
        for filme in filmes:
            print(filme)

    elif iniciar_aplicacao == 'b':
        if len(filmes) == 0:
            print(f'Você ainda não cadastrou nenhum filme.')
        else:
            todos_os_filmes = {titulo_buscar['titulo']: titulo_buscar for titulo_buscar in filmes}
            buscar = input('Informer o nome do filme que deseja buscar: ')

            if buscar in todos_os_filmes:
                print(todos_os_filmes[buscar])

    iniciar_aplicacao = input(MENU)

print('FIM DO PROGRAMA')
