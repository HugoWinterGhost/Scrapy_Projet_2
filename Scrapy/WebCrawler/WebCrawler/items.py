# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    pass

class ReviewAllocineItem(scrapy.Item):
  title = scrapy.Field()
  img = scrapy.Field()
  author = scrapy.Field()
  time = scrapy.Field()
  genre = scrapy.Field()
  score = scrapy.Field()
  desc = scrapy.Field()
  release = scrapy.Field()

class ReviewBoursoramaItem(scrapy.Item):
  indice = scrapy.Field()
  cours = scrapy.Field()
  var = scrapy.Field()
  hight = scrapy.Field()
  low = scrapy.Field()
  open_ = scrapy.Field()
  time = scrapy.Field()

class ReviewMangaItem(scrapy.Item):
  title = scrapy.Field()
  img = scrapy.Field()
  desc = scrapy.Field()
