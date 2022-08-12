from utils import database

MENU = """
#########################################
| - 'a' para adicionar um novo livro    |
| - 'l' para listar todos os livros     |
| - 'm' para marcar como lido um livro  |
| - 'd' para deletar um livro           |
| - 'q' para sair da aplicação          |
#########################################
Sua opção:"""


def menu():
    escolha_inicial = input(MENU).lower()
    while escolha_inicial != 'q':

        if escolha_inicial == 'a':
            nome = input('Informe o título do livro: ')
            autor = input('Informe o autor do título: ')
            database.adicionar_livro(nome, autor)

        elif escolha_inicial == 'l':
            database.mostrar_todos_os_livros()

        elif escolha_inicial == 'm':
            nome = input(f'Informe o título do livros que gostaria de marca como livro: ')
            database.marcar_livro_como_lido(nome)

        elif escolha_inicial == 'd':
            nome = input(f'Informe o livro que gostaria de deletar: ')
            database.deletar_um_livros(nome)

        escolha_inicial = input(MENU).lower()


if __name__ == '__main__':
    menu()
