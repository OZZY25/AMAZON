import requests
from bs4 import BeautifulSoup
from time import sleep

URL = 'https://www.amazon.com.mx/Huawei-MateBook-15-Pulgadas-Plateado/dp/B084DD3T5B/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=KU0XXH8LWCZY&dchild=1&keywords=huawei+matebook+d15&qid=1601238234&sprefix=huawei+mate%2Caps%2C525&sr=8-1'
headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id='title').get_text()
title = title.strip()
price = soup.find(id='priceblock_ourprice').get_text()

converted_price = price[1:7]
converted_price = converted_price.replace(',', '')
converted_price = float(converted_price)

while True:
    if converted_price < 17980:
        print('Change')
        break
    else:
        print('No Change')
    print(title)
    print(converted_price)
    sleep(10)
