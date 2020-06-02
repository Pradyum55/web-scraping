import csv
from urllib.request import urlopen as req
import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
url='https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'
class html:
    def __init__(self):
    def page(url):
        b=req(url)
        pagehtml=b.read()
        b.close()
        return soup(pagehtml,'html.parser')
pagesoup=html.page(url)
containers=pagesoup.findAll('div',{'class':'item-container'})
with open('products.csv','w') as f:
    head='brand,product name, shipping price\n'
    f.write(head)
    container=containers[0]

    for container in containers:
        brand=container.a.img["title"]
        title=container.findAll('a',{'class':'item-title'})
        name=title[0].text
        shipping=container.findAll('li',{'class':'price-ship'})
        ship=shipping[0].text.strip()
        print('brand' + brand)
        print('product name' + name)
        print('shipping price' + ship)
        f.write(brand +','+ name.replace(',','|') +','+ ship+'\n')
    
f.close()    

