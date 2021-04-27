# # Define here the models for your scraped items
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.exporters import PythonItemExporter
from scrapy.loader import ItemLoader 

class ClaroScrapItem(scrapy.Item):
    #define the fields for your item here like:
    #name = scrapy.Field()
    titulo = scrapy.Field()
    titulo_original = scrapy.Field()
    descripcion = scrapy.Field()
    lanzamiento = scrapy.Field()
    generos = scrapy.Field()
    duracion = scrapy.Field()
    ranking = scrapy.Field()
    clasificacion = scrapy.Field()
    tipo_venta = scrapy.Field()
    proveedor_contenido = scrapy.Field()
    proveedor_metadatos = scrapy.Field()

class ClaroScrapPrecioItem(scrapy.Item):
    #define the fields for your item here like:
    #name = scrapy.Field()
    precio = scrapy.Field()
    
