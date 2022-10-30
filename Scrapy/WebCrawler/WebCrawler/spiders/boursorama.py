import scrapy
import datetime
from scrapy import Request
from WebCrawler.items import ReviewBoursoramaItem

class BoursoramaSpider(scrapy.Spider):
  name = 'boursorama'
  allowed_domains = ['www.boursorama.com']
  
  # Liste des pages à collecter
  start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}' for n in range(1,3)]


  def parse_boursorama(self, response):
    liste_indices = response.css('table.c-table tr.c-table__row')[1:]

    # Boucle qui parcours l'ensemble des éléments de la liste des actions du CAC40
    for indice in liste_indices:
      item = ReviewBoursoramaItem()

      # Indice boursier
      try:
        item['indice'] = indice.css('td a.c-link::text')[0].extract()
      except:
        item['indice'] = 'None'
            
      # Indice cours de l'action
      try:
        item['cours'] = indice.css('td span.c-instrument--last::text')[0].extract().replace(' ', '')
      except:
        item['cours'] = 'None'

      # Variation de l'action
      try:
        item['var'] = indice.css('td span.c-instrument--instant-variation::text')[0].extract()
      except:
        item['var'] = 'None'
          
      # Valeur la plus haute
      try:
        item['hight'] = indice.css('td span.c-instrument--high::text')[0].extract()
      except:
        item['hight'] = 'None'

      # Valeur la plus basse
      try:
        item['low'] = indice.css('td span.c-instrument--low::text')[0].extract()
      except:
        item['low'] = 'None'

      # Valeur d'ouverture
      try:
        item['open_'] = indice.css('td span.c-instrument--open::text')[0].extract().replace(' ', '')
      except:
        item['open_'] = 'None'

      # Date de la collecte
      try:
        item['time'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      except:
        item['time'] = 'None'

      yield item

  def start_requests(self):
    for url in self.start_urls:
      yield Request(url = url, callback = self.parse_boursorama)
