import requests
import bs4
from urllib.parse import urljoin

from utils.book_handler import get_book_title, get_book_price, get_book_rating, get_book_url, get_img_url

BASE_URL = 'https://books.toscrape.com/'
URL = BASE_URL + 'catalogue/page-1.html'

titles = []
prices = []
ratings = []
book_urls = []
img_urls = []


while URL:
  response = requests.get(URL)
  soup = bs4.BeautifulSoup(response.text, 'html.parser')

  print(f'Now scraping: {URL}')

  # books contém os cards de todos os livros parseados
  books = soup.select('.product_pod')
  for book in books:
    # Titulo
    get_book_title(parsed_tag=book, css_selector='h3 > a', html_attribute='title', output_list=titles)

    # Preço
    get_book_price(parsed_tag=book, css_selector='.price_color', output_list=prices)

    # Avaliação
    get_book_rating(parsed_tag=book, css_selector='.star-rating', output_list=ratings)

    # Pagina do livro
    get_book_url(parsed_tag=book, css_selector='h3 > a', output_list=book_urls, base_url=BASE_URL)

    # Capa do livro
    get_img_url(parsed_tag=book, css_selector='.image_container > a > img', output_list=img_urls, base_url=BASE_URL)

    # next_page passa a ser o primeiro link do li com a classe .next (botão de next page) 
  next_page = soup.select_one('li.next > a')
  if next_page:
    # Se next_page existir na pagina atual, next_url é o atributo
    # href de next_page (o link ao qual ele leva)
    next_url = next_page['href']
    URL = urljoin(URL, next_url)
  else:
    URL = None

print('Total of titles:' + str(len(titles)))
print('Total of prices:' + str(len(prices)))
print('Total of ratings:' + str(len(ratings)))
print('Total of book urls:' + str(len(book_urls)))
print('Total of book images:' + str(len(img_urls)))