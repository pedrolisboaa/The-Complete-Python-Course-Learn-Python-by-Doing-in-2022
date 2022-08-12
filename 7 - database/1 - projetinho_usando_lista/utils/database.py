todo_os_livros = []


def adicionar_livro(nome, autor):
    if nome in todo_os_livros:
        print(f'O livro {nome} ja está cadastrado.')
        return

    novo_livro = {"nome": nome, "autor": autor, "lido": False}
    todo_os_livros.append(novo_livro)
    print(f'O livro {nome} foi cadastrado.')


def mostrar_todos_os_livros():
    if len(todo_os_livros) == 0:
        print(f'Não foram cadastrado nenhum livro.')
        return

    for livro in todo_os_livros:
        print(livro)


def marcar_livro_como_lido(nome):
    for livro in todo_os_livros:
        if livro['nome'] == nome:
            livro['lido'] = True
            print(f'O livros {nome} foi marcado como lido.')
        else:
            print(f'O livro {nome} não foi cadastrado.')


def deletar_um_livros(nome, livro=None):
    for livro in todo_os_livros:
        if livro[nome] == nome:
            todo_os_livros.remove(livro)



