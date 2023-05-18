import requests
import json
import re

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
        
        api = "https://www.enterprise.no/no/bilutleie/deals/mini-lease.html"
        base = "https://www.enterprise.no"
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        response = requests.get(api, headers=headers)
        tries = 0
        while "20" not in str(response.status_code):
            response = requests.get(f"{api}", timeout=(2, 60))
            tries += 1
            if tries > 3:
                print("no response enterprize")
                return None
        soup = BS(response.content, "html.parser")
        cars = soup.select(".cf.staggered-block")
        
        cleanCars = []
        match = "[^a-zA-Z0-9\n\.]"
        with open("car.json") as file:
            template = json.load(file)
        try:    
            for car in cars:
                public_id = f"{car.h2.text}{''.join(car.img['data-original'].split('.')[0:2])}"
                public_id = re.sub(match,'',public_id)
                cartemplate = template.copy()
                name = car.span.p.text
                if "eller lignende" in name:
                    name = name.replace(" eller lignende","")
                    price = car.select("p b")[0].text.replace(",- per måned", "").replace(".","")
                else:
                    name = car.h2.text
                    price = car.select("h2 b")[0].text.replace(",- per måned", "").replace(".","")
                cartemplate.update(
                    {
                        "site": "enterprise",
                        "name": name,
                        "make": name.split()[0],
                        "model": name.split()[1],
                        "drive": "Bensin",
                        "year": "Ukjent",
                        "seats": "Ukjent",
                        "transmission": "Automat",
                        "price": price,
                        "range": "Ukjent",
                        "location": ["oslo"],
                        "availability": "Available",
                        "includedkm": 1500,
                        "delivery": None ,
                        "fuelconsumption": None ,
                        "co2": None,
                        "binding": "1 mnd",
                        "order": f"{base}{car.a['href']}",
                        "img": cloudinary.uploader.upload(f"{base}{car.img['data-original']}", folder="enterprise", overwrite=False, public_id=public_id)["secure_url"],
                        "cargoVolume": None,
                        "engine": None,
                        "enginDescription": None,
                        "type": None
                    }
                )
                cleanCars.append(cartemplate)

        except Exception as e:
            print(e)
        

        return (cleanCars, )
