"-----------PARSING TASK2---------------"
import requests
from bs4 import BeautifulSoup as BS 


response = requests.get("http://www.example.com/")
html = response.text

def get_page_data(get_html):
    soup = BS(html, "lxml")
    site_title= soup.find('div').find('h1').text
    site_text = soup.find('div').find('p').text
    site_link = soup.find('a').get('href')
    print('h1:',site_title)
    print('p:',site_text)
    print('a:',site_link)

get_page_data(html)

"------------PARSING TASK3------------------"
import requests
from bs4 import BeautifulSoup as BS 


response = requests.get("https://www.wikipedia.org/")
html = response.text

def get_data(html):
    soup = BS(html,'lxml')
    de = soup.find('a', {'id': "js-link-box-de"}).text
    print(de)
get_data(html)

"--------------PARSING TASK4"
def getTitle(url):
    try:
        import requests
        from bs4 import BeautifulSoup as BS 

        response = requests.get(url)
        html = response.text
        soup = BS(html,'lxml')
        h1 = soup.find('div').find('h1')
        return h1
    except Exception:
        if h1 == None:
            print('Title could not be found')
print(getTitle('http://www.example.com/'))

def getTitle(url):
    
    import requests
    from bs4 import BeautifulSoup as BS 

    response = requests.get(url)
    html = response.text
    soup = BS(html,'lxml')
    h1 = soup.find('div').find('h1')
    
    if h1 != None:
        return h1
    else: 
        print('Title could not be found')
print(getTitle('https://www.w3resource.com/'))

import requests
from bs4 import BeautifulSoup as BS 

response = requests.get('https://enter.kg/')
html = response.text
soup = BS(html,'lxml')


"--------PARSING TASK 9"

# def get_categories():
#     category_list = []
#     category = soup.find_all('div', {'class':'moduletable'})
#     category_list.append(category.text)
# def_categories()
# print(category)

def getTitle(url):
    import requests
    from bs4 import BeautifulSoup as BS 

    response = requests.get(url)
    html = response.text
    soup = BS(html,'lxml')
    h1 = soup.find('div').find('h1')
    
    if response.status_code == 200:
        print(h1) 
    else: 
        print('Title could not be found')
getTitle('https://www.w3resource.com/')
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
import requests
from bs4 import BeautifulSoup as BS 
def getTitle(url):
    response = requests.get(url)
    html = response.text
    soup = BS(html,'lxml')
    h1 = soup.find('div').find('h1')
    return h1

h1 = getTitle('http://www.example.com/')   
if h1 == None:
        
    print("Title could not be found")
        
else:
      
    print(h1)