import requests
from Bot import Bot
from bs4 import BeautifulSoup as BS
import json


class Imove:
    def __init__(self):

        self.url = "https://secure.imove.no/cars"
        # self.postalcode = postalcode

    @classmethod
    def get_cars(cls, postalcode=None):
        headers = {"User-Agent": "My User Agent 1.0"}

        api = "https://secure.imove.no/api/vehicles"
        response = requests.get(f"{api}", headers=headers)
        tries = 0
        while "20" not in response:
            response = requests.get(f"{api}")
            tries += 1
            if tries > 3:
                break
        cars = response.json()
        available = [car for car in cars if car["isReserved"] == False]
        unavailable = [car for car in cars if car["isReserved"] == True]
        return (available, unavailable)

    @classmethod
    def get_cars_bot(cls, postalcode=None):
        api = "https://secure.imove.no/api/vehicles"
        bot = Bot()
        html = bot.get_html(api)[0]
        soup = BS(html, "lxml")
        cars = json.loads(soup.find("pre").text)
        available = [car for car in cars if car["isReserved"] == False]
        unavailable = [car for car in cars if car["isReserved"] == True]
        return (available, unavailable)
