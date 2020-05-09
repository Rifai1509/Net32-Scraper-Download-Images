import json, requests
from bs4 import BeautifulSoup
import pandas as pd

with open('dentarus_urls.json', 'r') as file:
    data =file.read()
urls = json.loads(data)

datas = []
for url in urls:
    r = requests.get(url[0]).text
    soup =  BeautifulSoup(r, 'html.parser')
    name = soup.find('h1', {'id':'ec-product-name'}).text.strip()
    price = soup.find('div','price-and-shipping-container').find('strong','current-price').text.strip()
    try:
        description = soup.find('div', {'id':'product-description-mobile'}).find('div','product-attributes-second-column').text
    except:
        description = 'No Description'
    table = soup.findAll('div','div-table')[1].findAll('div','product-attributes-second-column div-cell')
    try:
        code = table[1].text.strip()
    except:
        code = 'No Code'
    try:
        brand = table[2].text.strip()
    except:
        brand = 'No Brand'
    try :
        design = table[3].text.strip()
    except:
        design = 'No Design'
    try:
        firm = table[4].text.strip()
    except:
        firm = 'No Firmness'
    try:
        type = table[7].text.strip()
    except:
        type = 'No Type'
    try:
        image = f"https://www.net32.com{soup.find('div',{'id':'ec-pdp-image-container'}).find('img')['src']}"
    except:
        image = 'No Image'
    print(name)
    print(price)
    print(description)
    print(code)
    print(brand)
    print(design)
    print(firm)
    print(type)
    print(image)
    datas.append({'Name':name, 'Price':price,'Description':description, 'Manufacturer Code':code, 'Brand':brand, 'Design':design, 'Firmness':firm, 'Type':type,'Image Link':image})