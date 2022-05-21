import requests
from bs4 import BeautifulSoup
from random import randint

def tweet():
    offset = randint(0, 5538)
    html_doc = requests.get(f"http://biblioteca.agn.gob.do/cgi-bin/koha/opac-search.pl?idx=su&q=historia%20dominicana&offset={offset}&sort_by=relevance_dsc")
    soup = BeautifulSoup(html_doc.text,'html.parser')

    book_data = soup.find("a", "title").text.split(" /")
    tweet = f"Titulo: {book_data[0]} \n Autor: {book_data[1]}"
    return tweet