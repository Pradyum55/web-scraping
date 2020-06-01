import csv
from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup
a='https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'
b=req(a)
pagehtml=b.read()
b.close()
pagesoup=soup(pagehtml,'html.parser')

containers=pagesoup.findAll('div',{'class':'item-container'})
file='products.csv'
f=open(file,'w')

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
    
