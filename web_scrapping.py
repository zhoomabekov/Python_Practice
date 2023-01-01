import requests
from bs4 import BeautifulSoup

url = "https://www.kinopoisk.ru/lists/movies/top250/"

r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text,'lxml')
print(soup.text)
