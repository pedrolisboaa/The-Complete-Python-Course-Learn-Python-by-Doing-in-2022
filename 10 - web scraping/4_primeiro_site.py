import requests
from bs4 import BeautifulSoup

pagina = requests.get('http://www.metropoles.com.br')
sopa = BeautifulSoup(pagina.content, 'html.parser')

print(sopa.find('h1').text)
print(sopa.select_one('h3').text)
print(sopa.select_one('a').attrs['href'])
