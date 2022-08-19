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


class AnalisandoHTml:
    def __init__(self, page):
        self.page = BeautifulSoup(page, 'html.parser')

    def buscar_nome_do_livro(self):
        local = 'article.product_pod h3 a'  # localização pelo CSS
        link_livro = self.page.select_one(local)
        nome_livro = link_livro.attrs['title']

        return nome_livro

    def buscar_link_do_livro(self):
        local = 'article.product_pod div.image_container a'
        link = self.page.select_one(local)
        endereco_link = link.attrs['href']
        return endereco_link

    def buscar_preco_do_livro(self):
        valor_livro = float(self.page.find('p', {'class': 'price_color'}).string[1:])
        return valor_livro


if __name__ == '__main__':

    pagina = AnalisandoHTml(ITEM_HTML)

    print(pagina.buscar_preco_do_livro())
    print(pagina.buscar_nome_do_livro())
    print(pagina.buscar_link_do_livro())