import requests
from bs4 import BeautifulSoup as BS


class Swap:
    def __init__(self, postalcode: str):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        api = "https://swapacar.no/start"
        response = requests.get(f"{api}")
        tries = 0
        while "20" not in response:
            response = requests.get(f"{api}", timeout=(2, 60))
            tries += 1
            if tries > 3:
                break
        soup = BS(response.text, "lxml")
        available = []
        cars = soup.findAll("div", {"class": "fcar-list"})
        for car in cars:
            available.append(
                {
                    "title": car.find("div", {"class": "fcar-title"}).text,
                    "price": car.__dict__["attrs"]["data-price"],
                    "transmission": car.__dict__["attrs"]["data-transmission"],
                    "fuel": car.__dict__["attrs"]["data-powertrain"],
                }
            )
        return (available, None)

