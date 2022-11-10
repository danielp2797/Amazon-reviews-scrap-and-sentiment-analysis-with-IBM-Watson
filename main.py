from src.scraping.scraping import scrape, parse
from time import time
from selectorlib import Extractor
import csv
import sys

URL_PATH = 'data/url/urls.txt'
OUTPUT_PATH = 'data/reviews/raw/'
EXTRACTOR = Extractor.from_yaml_file('config/parser/selectors.yml')
TIMESTAMP = str(int(time()))
FIELDS = ["title", "content", "date", "variant", "images", "verified", "author", "rating", "product", "url"]

if __name__ == '__main__':

    url = str(sys.argv[1])
    url_protocol, url_domain = url.split('/')[0], url.split('/')[2]
    with open(OUTPUT_PATH+TIMESTAMP, 'w+') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        while True:
            data = scrape(url, EXTRACTOR)
            parse(data, writer)
            print(url)
            if data['next_page']:
                url = f'{url_protocol}//{url_domain}/'+data['next_page']
            else:
                break
