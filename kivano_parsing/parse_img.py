import requests

image_url = "https://cdn.britannica.com/77/235277-050-E9162647/white-bull-terrier-dog.jpg"

response = requests.get(image_url)


with open('mage.jpg', 'wb') as f:
    f.write(response.content)
