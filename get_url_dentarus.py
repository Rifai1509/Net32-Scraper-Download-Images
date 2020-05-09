from bs4 import BeautifulSoup
import requests
import  json
urls = []

url = 'https://www.net32.com/search?q=dentatus'
headers = {
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Host': 'www.net32.com',
'Pragma': 'no-cache',
'Referer': 'https://www.net32.com/search?q=dentatus',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
r= requests.get(url,headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
products = soup.findAll('div','localsearch-result-product-details-area')
print(products)
for p in products:
    url = f"https://www.net32.com/{p.find('div','localsearch-result-product-name-container').find('a')['href']}"
    print(url)
    urls.append([url])
with open(f'dentarus_urls.json', 'w') as file:
    json.dump(urls, file)
