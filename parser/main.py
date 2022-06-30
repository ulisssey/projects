from fake_useragent import UserAgent
import requests
import json


ua = UserAgent()


def get_data():
    cookies = {
        'cna': 'LAjmGXapSVMCASVjbbXNvZBF',
        '_ym_uid': '1633622573689041220',
        'intl_locale': 'ru_RU',
        'aer_abid': '4e4c8194263e2b72',
        'tmr_lvid': '3ea471068ff3f3b3cc7dcb6b40b99bfd',
        'tmr_lvidTS': '1639753110156',
        '_ym_d': '1650872835',
        'aep_usuc_t': 'ber_l=A1',
        'bx_s_t': 'SYV1lYu3SwVXp8Q8GLQ/z+soAlFfs+cg57VldDn8mulJr0pt9SQsNz8uv+NbYtg5K8KStGMQZd175d9ILRBY7DibBWy/o+3cVfHey9HFza4=',
        'aep_common_f': '84D4waqs91n8cubwIQhlvdTKNOnty0PVNr9dWTqzRXOls5bRFswZSQ==',
        'aer_ab': '19',
        '_gcl_au': '1.1.344000470.1650943088',
        '_ga_VED1YSGNC7': 'GS1.1.1650943087.1.1.1650944080.0',
        '_ga': 'GA1.2.818197896.1650872835',
        'xman_f': 'XeCT6v+KYdMNjmu6SXMRBA2VYW/2AW1tWZzIcjRDSgHUxwjOJPf+5QZo3BoduRdwGEVdvUBKqL4RDPr2TAlwJF1xTo/M0WPxHYzgnmmDMm+8lIKIC5Mqz49Iljmg3aXzeNqPYl+MJT9zE+sBqo9Y7oWV9E+uiENz7S4/JZTZecC7dAhDjnF5JCVLm26yXI3kbpkGUE3TFvaDPeSVxFzlMcm4nEvKN2wWVWhuS+jgdQ+ae0wxqpP/iyyabKy84veA9vfT43wuP+0uPl7i050n9TLIITQgSBQReedQKLGzIZq6tc5GiE5JzPjjeA++cMbMnLudQXNN4YHKYqKs9SIQ1Nj9bLOphYFIIHV9SYgB8gZLKj5AsSpzFZmEO9WJ9vNioInc4bpE7ukpinTiul9FakPbGMt44Xmo',
        'aep_usuc_f': 'isfm=y&site=rus&c_tp=KZT&x_alimid=725485726&re_sns=google&isb=y&region=KZ&b_locale=ru_RU',
        'acs_usuc_t': 'x_csrf=12z0q8org1zxe&acs_rt=95537d0fa32b4c56b1cbe97c504fff90',
        'xman_t': 'eVRrQesBRBqzqvxrUexwu4LrswK7XjZazyMEqxBAZ05qKGI2HZ4ckF54kFprprKb',
        'xman_us_f': 'x_locale=ru_RU&x_l=0&last_popup_time=1650872849006&x_user=KZ|Erasyl|Turlybek|ifm|725485726&no_popup_today=n&x_lid=kz1107052084oytq&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1656588895963%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=298095570d014c969dcad2392420b71b',
        '_gid': 'GA1.2.16545515.1656588599',
        '_gat_UA-164782000-1': '1',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'xlly_s': '1',
        'JSESSIONID': '6DC596BAF9D71767995E0210A94E0737',
        'tmr_detect': '1%7C1656588634130',
        'tmr_reqNum': '304',
        'intl_common_forever': 'ujM39GOs6ZKg6Qo5FEedcDw8RntHWgE6dmaGUocNfa9fNYq5qC1FtQ==',
        'tfstk': 'cigGBmG7NcrsG2ZnVFa6kQJjEJKRZU-QIz4n8CJnzsSKOf3Fi7jF41NA_JpWQi1..',
        'l': 'eBTe8-gIgljtgLrfBOfwourza77OSIRAguPzaNbMiOCP_HfH5HWVB6bIyL8MC3MNh6KDR3Wrj_IwBeYBqIXhHrQNAdzNp9Hmn',
        'isg': 'BFVVggc6mynK7bxU4j0XVz9OZFEPUglkOLueMdf6EUwbLnUgn6IZNGPo-CqYLiEc',
    }

    headers = {
        'authority': 'aliexpress.ru',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cna=LAjmGXapSVMCASVjbbXNvZBF; _ym_uid=1633622573689041220; intl_locale=ru_RU; aer_abid=4e4c8194263e2b72; tmr_lvid=3ea471068ff3f3b3cc7dcb6b40b99bfd; tmr_lvidTS=1639753110156; _ym_d=1650872835; aep_usuc_t=ber_l=A1; bx_s_t=SYV1lYu3SwVXp8Q8GLQ/z+soAlFfs+cg57VldDn8mulJr0pt9SQsNz8uv+NbYtg5K8KStGMQZd175d9ILRBY7DibBWy/o+3cVfHey9HFza4=; aep_common_f=84D4waqs91n8cubwIQhlvdTKNOnty0PVNr9dWTqzRXOls5bRFswZSQ==; aer_ab=19; _gcl_au=1.1.344000470.1650943088; _ga_VED1YSGNC7=GS1.1.1650943087.1.1.1650944080.0; _ga=GA1.2.818197896.1650872835; xman_f=XeCT6v+KYdMNjmu6SXMRBA2VYW/2AW1tWZzIcjRDSgHUxwjOJPf+5QZo3BoduRdwGEVdvUBKqL4RDPr2TAlwJF1xTo/M0WPxHYzgnmmDMm+8lIKIC5Mqz49Iljmg3aXzeNqPYl+MJT9zE+sBqo9Y7oWV9E+uiENz7S4/JZTZecC7dAhDjnF5JCVLm26yXI3kbpkGUE3TFvaDPeSVxFzlMcm4nEvKN2wWVWhuS+jgdQ+ae0wxqpP/iyyabKy84veA9vfT43wuP+0uPl7i050n9TLIITQgSBQReedQKLGzIZq6tc5GiE5JzPjjeA++cMbMnLudQXNN4YHKYqKs9SIQ1Nj9bLOphYFIIHV9SYgB8gZLKj5AsSpzFZmEO9WJ9vNioInc4bpE7ukpinTiul9FakPbGMt44Xmo; aep_usuc_f=isfm=y&site=rus&c_tp=KZT&x_alimid=725485726&re_sns=google&isb=y&region=KZ&b_locale=ru_RU; acs_usuc_t=x_csrf=12z0q8org1zxe&acs_rt=95537d0fa32b4c56b1cbe97c504fff90; xman_t=eVRrQesBRBqzqvxrUexwu4LrswK7XjZazyMEqxBAZ05qKGI2HZ4ckF54kFprprKb; xman_us_f=x_locale=ru_RU&x_l=0&last_popup_time=1650872849006&x_user=KZ|Erasyl|Turlybek|ifm|725485726&no_popup_today=n&x_lid=kz1107052084oytq&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1656588895963%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=298095570d014c969dcad2392420b71b; _gid=GA1.2.16545515.1656588599; _gat_UA-164782000-1=1; _ym_isad=1; _ym_visorc=b; xlly_s=1; JSESSIONID=6DC596BAF9D71767995E0210A94E0737; tmr_detect=1%7C1656588634130; tmr_reqNum=304; intl_common_forever=ujM39GOs6ZKg6Qo5FEedcDw8RntHWgE6dmaGUocNfa9fNYq5qC1FtQ==; tfstk=cigGBmG7NcrsG2ZnVFa6kQJjEJKRZU-QIz4n8CJnzsSKOf3Fi7jF41NA_JpWQi1..; l=eBTe8-gIgljtgLrfBOfwourza77OSIRAguPzaNbMiOCP_HfH5HWVB6bIyL8MC3MNh6KDR3Wrj_IwBeYBqIXhHrQNAdzNp9Hmn; isg=BFVVggc6mynK7bxU4j0XVz9OZFEPUglkOLueMdf6EUwbLnUgn6IZNGPo-CqYLiEc',
        'origin': 'https://aliexpress.ru',
        'referer': 'https://aliexpress.ru/category/202000006/computer-office.html?spm=a2g2w.home.104.1.5a50501dmZ78QA',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    json_data = {
        'categoryIds': '202000006',
        'currencyType': 'RUB',
        'keyword': '',
        'count': 60,
        'offset': 0,
        'p4pId': '71c82b38-e5a0-4b2a-889f-c35590570ed5',
    }

    response = requests.post('https://aliexpress.ru/aer-webapi/v1/recommend', cookies=cookies, headers=headers, json=json_data).json()
    products_json = response.get('data').get('productsFeed').get('products')


    with open('result.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products = []
    products_json = response.get('data').get('productsFeed').get('products')
    for product in products_json:
        product_id = product.get('id')
        product_title = product.get('productTitle')
        product_url = product.get('productUrl')
        product_fullprice = product.get('fullPrice')
        product_discount = product.get('discount')
        product_finalprice = product.get('finalPrice')
        products.append({'id': product_id, 'title': product_title, 'url': product_url, 'fullPrice': product_fullprice, 'discount': product_discount, 'finalPrice': product_finalprice})


    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()