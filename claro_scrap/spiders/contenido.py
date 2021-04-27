import scrapy
import json
from pprint import pprint
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from claro_scrap.items import ClaroScrapItem
from claro_scrap.items import ClaroScrapPrecioItem

class ContenidoSpider(scrapy.Spider):
    name = 'contenido'
    allowed_domains = ['clarovideo.com']
    start_urls = ['https://mfwkweb-api.clarovideo.net/services/content/data?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=obmedikfqi5keapnqholeeh3b1&group_id=708158']

    def parse(self, response):

        item = ItemLoader(ClaroScrapItem(), response)

        results = json.loads(response.body)
        contenidos = results.get('response').get('group')

        item.add_value('titulo', contenidos.get("common").get("title"))
        item.add_value('titulo_original', contenidos.get("common").get("extendedcommon").get("media").get("originaltitle"))
        item.add_value('descripcion', contenidos.get("common").get("extendedcommon").get("media").get("description_extended"))
        item.add_value('lanzamiento', contenidos.get('common').get('extendedcommon').get('media').get('publishyear'))
        item.add_value('generos', [
                    contenidos.get('common').get('extendedcommon').get('genres').get('genre')[0].get('name'),
                    contenidos.get('common').get('extendedcommon').get('genres').get('genre')[1].get('name'),
                    contenidos.get('common').get('extendedcommon').get('genres').get('genre')[2].get('name')
                    ])
        item.add_value('duracion', contenidos.get('common').get('duration'))
        item.add_value('ranking', contenidos.get('common').get('ranking').get('average_votes'))
        item.add_value('clasificacion', contenidos.get('common').get('extendedcommon').get('media').get('rating').get('code'))
        item.add_value('tipo_venta', contenidos.get('common').get('extendedcommon').get('format').get('sell_type'))
        item.add_value('proveedor_contenido', [
                    contenidos.get('universal_id').get('content_providers')[0].get('provider_code'),
                    contenidos.get('universal_id').get('content_providers')[1].get('provider_code'),
                    contenidos.get('universal_id').get('content_providers')[2].get('provider_code')
                    ])
        item.add_value('proveedor_metadatos', contenidos.get('universal_id').get('metadata_providers').get('gracenote').get('provider_code'))

        yield item.load_item()



    



    

