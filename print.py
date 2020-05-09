import json, requests
from bs4 import BeautifulSoup

with open('dentarus_urls.json', 'r') as file:
    data =file.read()
urls = json.loads(data)

num = 0
for url in urls:
    num += 1
    if num == 10:
        break
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
        tipe = table[7].text.strip()
    except:
        tipe = 'No Type'

#    print(name)
#    print(price)
    print(description)
    print("Features and Benefits")
    print('Manufacture Code :', code)
    print('Brand:', brand)
    print('Design:', design)
    print('Firmness :', firm)
    print('Type :', tipe)
    print('\n')
    
#    print(image)