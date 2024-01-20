from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json
import telepot

url = "https://onepieceex.net/"
bs = BeautifulSoup(urlopen(url), 'html.parser')

def search_pages():
    search_pages = bs.find_all("a")
    for page in pages:
        if "episódios" in page:
            temporadas = page["href"]
            return temporadas

temporadas_url = f"{base_url}{search_pages()}"
print(temporadas_url)