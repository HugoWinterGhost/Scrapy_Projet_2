import scrapy
from scrapy import Request
from WebCrawler.items import ReviewMangaItem

class MangaSpider(scrapy.Spider):
  name = 'manga'
  allowed_domains = ['www.myanimelist.net']

  # Liste des pages à collecter
  start_url = [f'https://myanimelist.net/manga.php?letter=A']


  def parse_boursorama(self, response):
    liste_mangas = response.css('div.list table tr')[1:]

    # Boucle qui parcours l'ensemble des éléments de la liste des actions du CAC40
    for manga in liste_mangas:
      item = ReviewMangaItem()

      # Nom de l'animé
      try:
        item['title'] = manga.css('td strong::text')[0].extract()
      except:
        item['title'] = 'None'
            
      # Lien de l'image de l'animé
      try:
        item['img'] = manga.css('td img')[0].attrib['data-src']
      except:
        item['img'] = 'None'

      # Description de l'animé
      try:
        item['desc'] = manga.css('td div.pt4::text')[0].extract()
      except:
        item['desc'] = 'None'

      yield item

  def start_requests(self):
    for url in self.start_url:
      yield Request(url = url, callback = self.parse_boursorama)
