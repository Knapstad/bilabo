import requests
import json

from bs4 import BeautifulSoup as BS

import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name = "bilabonnement",
  api_key = "179299515168542",
  api_secret = "hQr86XL5c_RErMiffv5kf_eOy4c" ,
  secure = True
)

class Enterprise:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls):
        try:
            api = "https://www.enterprise.no/no/bilutleie/deals/mini-lease.html"
            base = "https://www.enterprise.no"
            response = requests.get(api)
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response volvo")
                    return None
            soup = BS(response.content, "html.parser")
            cars = soup.select(".cf.staggered-block")
            cleanCars = []
            with open("car.json") as file:
                template = json.load(file)
            for car in cars:
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "enterprise",
                        "name": car.h2.text,
                        "make": car.h2.text.split()[0],
                        "model": car.h2.text.split()[1],
                        "drive": "Bensin",
                        "year": "Ukjent",
                        "seats": "Ukjent",
                        "transmission": "Automat",
                        "price": car.select("p b")[0].text.replace(",- per måned", "").replace(".",""),
                        "range": "Ukjent",
                        "location": ["Oslo"],
                        "availability": "Available",
                        "includedkm": 1500,
                        "delivery": None ,
                        "fuelconsumption": None ,
                        "co2": None,
                        "binding": "1 mnd",
                        "order": f"{base}{car.a['href']}",
                        "img": cloudinary.uploader.upload(f"{base}{car.img['data-original']}", folder="enterprise", overwrite=False, public_id=f"{car.h2.text}{''.join(car.img['data-original'].split('.')[0:2])}")["secure_url"],
                        "cargoVolume": None,
                        "engine": None,
                        "enginDescription": None,
                        "type": None
                    }
                )
                cleanCars.append(cartemplate)

        except Exception as e:
            print(e)
            return None

        return (cleanCars, )
