import requests
from bs4 import BeautifulSoup
import pandas as pd


articles = []


def extract(page):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://bilki.bg/bilki-i-chaj.html?p={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_='item-content')
    for item in divs:
        title = item.find('h2').text.strip()
        image = item.find('img')['src']
        price = item.find('span', class_='price').text.strip()
        description = item.find('div', class_='short-description').text.strip()

        article = {
            'title': title,
            'image': image,
            'price': price,
            'description': description
        }
        articles.append(article)
    return


for i in range(1, 68):
    print(f'Getting pages {i}')
    c = extract(i)
    transform(c)

df = pd.DataFrame(articles)
print(df.head())
df.to_csv('chai.csv')