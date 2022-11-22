import requests
from bs4 import BeautifulSoup as BS

response = requests.get("https://www.kivano.kg/")
# print(response.status_code)
# print(type(response.text))

html = response.text
soup = BS(html,"lxml")
print(dir(soup))
# print(soup.find('a'))
product_box = soup.find('div',{'class': 'product_box'})

def get_product_data(product_box:BS) -> dict:
    title = product_box.find('div',{'class': 'product_title'}).text
    # print(title.text)
    # find price:
    price = product_box.find('div',{'class':"product_price"}).text.strip()
    print(price)
    # find photo link
    image = product_box.find('div',{'class':"product_img"}).find('img').get('src')
    # print(image)
    return {'title':title,'price':price,'image':image}
def get_all_products(soup:BS):
    products = []
    for product_box in soup.find_all('div',{'class':'product_box'}):
        product_data = get_product_data(product_box)
        products.append(product_data)
    return products
def get_soup(url:str) -> BS:
    response = requests.get(url)
    html = response.text
    soup = BS(html,"lxml")
    return soup

def write_to_json(data):
    import json
    with open('db.json','w', encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False)

def main():
    soup = get_soup("https://www.kivano.kg/")
    products = get_all_products(soup)
    for p in products:
        print(p)
    # OR print(products)
    write_to_json(products)
main()