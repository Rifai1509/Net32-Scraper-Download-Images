from bs4 import BeautifulSoup
import requests
import  json
urls = []
for page in range(1,4):
    url = f'https://www.net32.com/search?filter.manufacturer=Sunstar&page={page}'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.net32.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.net32.com/search?filter.manufacturer=Sunstar',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'

    }
    r= requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    products = soup.findAll('div','localsearch-result-wrapper localsearch-result-data-element')
    print(products)
#     for p in products:
#         url = f"https://www.net32.com/{p.find('div','localsearch-result-product-name-container').find('a')['href']}"
#         print(url)
#         urls.append([url])
# with open(f'../url.json', 'w') as file:
#     json.dump(urls, file)
