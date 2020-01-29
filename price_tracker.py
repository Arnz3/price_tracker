import webbrowser
import bs4
import requests


def track_price(part, URL):
    res = requests.get(URL)
    if res.raise_for_status == none:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        elems = soup.select(//*[@id="priceblock_ourprice"])
        price = elems[0].text.strip()
    else:
        return fout
