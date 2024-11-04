import subprocess
import os

def run_scrapy():
    scrapy_command = [
        'scrapy', 'crawl', 'allocine', '-o', 'films.csv', '-t', 'csv'
    ]
    cwd = os.path.join(os.path.dirname(__file__), '..', 'allocine_scraper')
    subprocess.run(scrapy_command, cwd=cwd)