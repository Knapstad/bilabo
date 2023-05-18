import json
import re
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

class Flexidrive:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://www.flexidrive.no"
            api = "https://www.flexidrive.no/vare-biler"
            response = requests.get(f"{api}")
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response flex")
                    return None
            soup = BS(response.text, "lxml")
            cars = soup.find_all("div", {"class": "collection-item-2 w-dyn-item"})

            cleanCars = []
            match = "[^a-zA-Z0-9\n\.]"
            with open("car.json") as file:
                template = json.load(file)
            for car in cars:
                img = car.find("img",{"class": "image-3"})["src"]
                public_id = f'{car.find("h4").text}{img.split("/")[-1]}'
                public_id = re.sub(match,'', public_id)
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "flexidrive",
                        "name": car.find("h4").text,
                        "make": car.find("h4").text.split()[0],
                        "model": car.find("h4").text.split()[-1],
                        "drive": car.find_all("div",{"class": "paragraph"})[2].text,
                        "year": car.find_all("div",{"class": "paragraph"})[0].text,
                        "seats": car.find_all("div",{"class": "paragraph"})[3].text,
                        "transmission":car.find_all("div",{"class": "paragraph"})[1].text,
                        "price": car.find("p",{"class": "paragraph-6"}).text,
                        "range": car.get("range", ""),
                        "kmMonth": "1500",
                        "location": ["sandnes","stavanger"],
                        "availability": False if car.find_all("div", {"class": "w-condition-invisible"}) else "available",
                        "order": f'{base}{car.find("a", {"class": "button-2"})["href"]}',
                        "img": cloudinary.uploader.upload(img, folder="flexidrive", overwrite=False, public_id=public_id)["secure_url"],
                        "cargoVolume": car.get("cargoVolume", ""),
                    }
                )
                cleanCars.append(cartemplate)

            available = [car for car in cleanCars if car.get("availability", 0)]
            unavailable = [car for car in cleanCars if not car.get("availability", 0)]
            return (available, unavailable)
        except Exception as e:
            print(e)
            return None