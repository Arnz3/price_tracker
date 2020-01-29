import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B07SXMZLPK?tag=pcpapi-20&linkCode=ogi&th=1&psc=1"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle")
print(title)
