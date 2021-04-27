import scrapy
import json
from pprint import pprint
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from claro_scrap.items import ClaroScrapItem
from claro_scrap.items import ClaroScrapPrecioItem

class PrecioSpider(scrapy.Spider):
    name = 'precio'
    allowed_domains = ['clarovideo.com']
    start_urls = ['https://mfwkweb-api.clarovideo.net/services/payway/purchasebuttoninfo?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=obmedikfqi5keapnqholeeh3b1&group_id=708158']  
    
    def parse(self, response):

        item = ItemLoader(ClaroScrapPrecioItem(), response)

        results = json.loads(response.body)
        response = results.get('response')

        item.add_value('precio', response.get("listButtons").get("button")[0].get("price"))

        yield item.load_item()



    



    

