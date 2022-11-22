import requests
import lxml
from bs4 import BeautifulSoup as BS

main_url = 'https://24.kg'

def get_soup(url):
    html = requests.get(url).text
    soup = BS(html, 'lxml')
    return soup

def get_categories():
    soup = get_soup(main_url)
    cat_block = soup.find('ul', class_="nav navbar-nav")
    category_tags = cat_block.find_all('a')
    return [tag.get('href') for tag in category_tags]

def get_news_title(cat_url):
    soup = get_soup(main_url + cat_url)
    titles = soup.find_all('div', class_="one")
    return [div.find('a').get('href') for div in titles]

# main_url + /vlast/qwertyui
def get_news_article(news_url):
    soup = get_soup(main_url + news_url)
    article_body = soup.find('div', {"itemprop":"articleBody"}) 
    return article_body.text

import csv
def write_to_csv(data):
    with open('news.csv', 'a') as file:
        writer = csv.writer(file, dialect = 'excel')
        writer.writerow([data])

import json
def write_to_json(data):
    with open('news.json', 'a') as file:
        json_ = json.dumps(data, ensure_ascii=False) + '\n'
        file.write(json_)


def main():
    category_urls = get_categories()
    for cat_url in category_urls:
        news_urls = get_news_title(cat_url)
        for news_url in news_urls:
            res_text = get_news_article(news_url)
            # write_to_csv(res_text)
            write_to_json(res_text)
print(main())