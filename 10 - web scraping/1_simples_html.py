from bs4 import BeautifulSoup

HTML_SIMPLES = """
<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class1</p>
<p>Here's another p without a class2</p>
<p>Here's another p without a class3</p>
<ul>
    <a class="sister" href="http://example.com/elsie1" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/elsie2" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/elsie3" id="link1">Elsie</a>


</ul>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>
"""

soup_simples = BeautifulSoup(HTML_SIMPLES, 'html.parser')


def procurar_titulo():
    h1 = soup_simples.find('h1')
    return h1.string


def procurar_itens_de_lista():
    lista = []
    li = soup_simples.find_all('li')
    for item in li:
        lista.append(item.text)

    return lista


def procurar_paragrafo_com_classe():
    paragrafo = soup_simples.find('p', {"class": "subtitle"}).string
    return paragrafo


def procurando_todos_os_links():
    a = soup_simples.find_all('a')
    for _ in a:
        print(_.get('href'))


print(procurar_titulo())
print((procurar_itens_de_lista()))
print(procurar_paragrafo_com_classe())
procurando_todos_os_links()
