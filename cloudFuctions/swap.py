import requests
from bs4 import BeautifulSoup as BS


class Swap:
    def __init__(self, postalcode: str = None):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://swapacar.no"
            api = "https://swapacar.no/start"
            response = requests.get(f"{api}")
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response swap")
                    return None
            soup = BS(response.text, "lxml")
            available = []
            cars = soup.findAll("div", {"class": "fcar-list"})
            for car in cars:
                details = car.find("div", {"class": "fcar-sdesc"}).text.split("|")
                available.append(
                    {
                        "site": "swap",
                        "name": car.find("div", {"class": "fcar-title"}).text,
                        "make": car.find("div", {"class": "fcar-title"}).text.split()[
                            0
                        ],
                        "model": " ".join(
                            car.find("div", {"class": "fcar-title"}).text.split()[1:]
                        ),
                        "drive": details[2],
                        "year": details[0],
                        "seats": details[1],
                        "transmission": details[3],
                        "price": int(float(car.__dict__["attrs"]["data-price"])),
                        "range": "",
                        "kmMonth": details[-1],
                        "location": ["Oslo"],
                        "availability": "Available",
                        "order": f'{base}{car.find("div", {"class": "fcar-btn"}).a["href"]}',
                        "img": car.find("img")["src"],
                        "cargoVolume": "",
                    }
                )
            return (available,)
        except Exception as e:
            print(e)
            return None

