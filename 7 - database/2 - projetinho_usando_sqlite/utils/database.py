import sqlite3

def adicionar_livro(titulo, autor):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO livros VALUES (?, ?, ?)', (titulo, autor, 0))
    conexao.commit()

    conexao.close()


def mostrar_todos_os_livros():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    todos_livros = cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    for livro in livros:
        print(livro)

    conexao.close()


def marcar_livro_como_lido(titulo):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute('UPDATE livros SET lido="1" WHERE titulo=?', (titulo,))
    conexao.commit()

    conexao.close()


def deletar_um_livros(titulo):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM livros WHERE titulo=?', (titulo,))
    conexao.commit()

    conexao.close()
