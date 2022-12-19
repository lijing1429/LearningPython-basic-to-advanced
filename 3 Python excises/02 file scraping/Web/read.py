import requests
from bs4 import BeautifulSoup

URL = "https://www.po18vip.uk/read/58319/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)