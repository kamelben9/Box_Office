import sys
import os
from scrapy.crawler import CrawlerProcess

# Ajouter le chemin du projet Scrapy au chemin Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'allocine_scraper'))

# Importer le spider Scrapy
from allocine_scraper.spiders.allocine_spider import AllocineSpider

def run_allocine_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            os.path.join(os.path.dirname(__file__), 'films.json'): {"format": "json"},
        },
    })
    process.crawl(AllocineSpider)
    process.start()