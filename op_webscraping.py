from urllib import request, parse
from bs4 import BeautifulSoup
import time
import json
import telepot
import re

def webscraping():
    base_url = "https://onepieceex.net"
    requisicao = request.Request(base_url + "/episodios", headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    url = request.urlopen(requisicao)
    bs = BeautifulSoup(url, 'html.parser')
    #bs_json = json.loads("".join(bs.contents))
    search_titles = bs.find_all("h2", {'class': 'caps'})

    # Making sure we got the result that we wished for and appending them to a list
    titles = []
    for title in search_titles:
        print(title.text)
        titles.append(title.text)

    #pattern = re.compile("/episodios/")
    links = bs.find_all("a")
    endpoints = []

    for link in links:
        if "/episodios/t" in link["href"]:
            endpoints.append(link["href"])
    # Making sure once again we got the desired content, this time in 'endpoints'
    #print(endpoints)

    temporadas = []
    
    for title, endpoint in zip(titles, endpoints):
        temporada = title
        endpoint_url = base_url + endpoint
        #print(temporada + ": " + endpoint_url)

        if title != titles[-1]:
            temporada = f"{temporada}: {endpoint_url}"
        else:
            temporada = f"{temporada}: {endpoint_url}"

        temporadas.append(temporada)
    
    return temporadas