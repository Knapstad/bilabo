import json
import requests

from bs4 import BeautifulSoup as BS
import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name = "bilabonnement",
  api_key = "179299515168542",
  api_secret = "hQr86XL5c_RErMiffv5kf_eOy4c" ,
  secure = True
)


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
            with open("car.json") as file:
                template = json.load(file)
            for car in cars:
                details = car.find("div", {"class": "fcar-sdesc"}).text.split("|")
                name = car.find("div", {"class": "fcar-title"}).text
                img = car.find("img")["src"]
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "swap",
                        "name": name,
                        "make": "land rover" if car.find("div", {"class": "fcar-title"}).text.split()[
                            0].lower() == "land" else  car.find("div", {"class": "fcar-title"}).text.split()[
                            0],
                        "model": " ".join(
                            car.find("div", {"class": "fcar-title"}).text.split()[1:]
                        ).replace("Rover ", ""),
                        "drive": details[2] if details[2].lower() != "phev" else "hybrid",
                        "year": details[0] if details[0] else "ukjent års",
                        "seats": details[1],
                        "transmission": details[3],
                        "price": int(float(car.__dict__["attrs"]["data-price"])),
                        "range": "",
                        "kmMonth": 1200,
                        "location": ["Oslo"],
                        "availability": "Available",
                        "order": f'{base}{car.find("div", {"class": "fcar-btn"}).a["href"]}',
                        "img": cloudinary.uploader.upload(img, folder="swap", overwrite=False, publicid=f"{name}{img}.split('/')[-1].split('?')[0]")["secure_url"],
                        "cargoVolume": "",
                    }
                )
                available.append(cartemplate)
            return (available,)
        except Exception as e:
            print(e)
            return None

