import requests
from bs4 import BeautifulSoup
import json


products = []
# url = 'https://www.ayanmarket.kz/collection/ovoschi/'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }


# response = requests.get(url, headers=headers)
with open('parser2/index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_titles = soup.find_all(class_='dis-product_card__title_link')
all_product_prices = soup.find_all(class_='dis-product_card__price')
for i in range(len(all_products_titles)):
    products.append(
            {all_products_titles[i].text.strip(): all_product_prices[i].text.strip()}
        )

with open ('parser2/products.json', 'w') as file:
    json.dump(products, file, indent=4, ensure_ascii=False)