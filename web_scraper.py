# scraping a webpage
import requests as rq
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com/'
response = rq.get(url)
soup = bs(response.text, 'lxml')

print(soup)

# exploring webpage HTML

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')


for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)
    print('\n')
