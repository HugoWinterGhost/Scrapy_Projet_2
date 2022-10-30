import scrapy
from scrapy import Request
from WebCrawler.items import ReviewAllocineItem


class AllocineSpider(scrapy.Spider):
  name = 'allocine'
  allowed_domains = ['www.allocine.fr']
  
  # Liste des pages à collecter
  start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1,10)]


  def parse_allocine(self, response):
    liste_film = response.css('ol li.mdl')

    # Boucle qui parcours l'ensemble des éléments de la liste des films
    for film in liste_film:
      item = ReviewAllocineItem()

      # Nom du film
      try:
        item['title'] = film.css('h2 a::text')[0].extract()
      except:
        item['title'] = 'None'
            
      # Lien de l'image du film
      try:
        item['img'] = film.css('img')[0].attrib['src']
      except:
        item['img'] = 'None'

      # Auteur du film
      try:
        item['author'] = film.css('a.blue-link::text')[0].extract()
      except:
        item['author'] = 'None'
          
      # Durée du film
      try:
        item['time'] = film.css('div.meta-body-item.meta-body-info::text')[0].extract().replace('\n', '')
      except:
        item['time'] = 'None'

      # Genre cinématographique
      try:
        item['genre'] = [element.extract() for element in film.css('div.meta-body-item.meta-body-info span::text')][1:]
      except:
        item['genre'] = 'None'

      # Score du film
      try:
        item['score'] = film.css('div.rating-item-content span.stareval-note::text')[0].extract()
      except:
        item['score'] = 'None'

      # Description du film
      try:
        item['desc'] = film.css('div.synopsis div.content-txt::text')[0].extract().replace('\n', '')
      except:
        item['desc'] = 'None'

      # Date de sortie
      try:
        item['release'] = film.css('div.meta-body-item span.date::text')[0].extract()
      except:
        item['release'] = 'None'

      yield item

  def start_requests(self):
    for url in self.start_urls:
      yield Request(url = url, callback = self.parse_allocine)
