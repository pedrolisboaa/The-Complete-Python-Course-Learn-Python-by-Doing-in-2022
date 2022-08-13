import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def buscar_nome_do_livro():
    local = 'article.product_pod h3 a'  # localização pelo CSS
    link_livro = soup.select_one(local)
    nome_livro = link_livro.attrs['title']

    return nome_livro


def buscar_link_do_livro():
    local = 'article.product_pod div.image_container a'
    link = soup.select_one(local)
    endereco_link = link.attrs['href']
    return endereco_link


def buscar_preco_do_livro():
    valor_livro = float(soup.find('p', {'class': 'price_color'}).string[1:])
    return valor_livro






print(buscar_nome_do_livro())
print(buscar_link_do_livro())
print(buscar_preco_do_livro())
print(type(buscar_preco_do_livro()))
