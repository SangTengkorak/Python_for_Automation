# preparing for multipages websraping

from bs4 import BeautifulSoup as bs
import requests as rq

url = 'https://scrapingclub.com/exercise/list_basic/?page=2'
response = rq.get(url)
soup = bs(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1

# for i in items:
#     itemName = i.find('h4', class_='card-title').text.strip('\n')
#     itemPrice = i.find('h5').text
#     print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
#     count += 1

# scraping multiple pages
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

# print(urls)

count = 1
for i in urls:
    newUrl = url + i
    response = rq.get(newUrl)
    soup = bs(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count += 1
