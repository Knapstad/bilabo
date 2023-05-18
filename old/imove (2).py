from typing import Dict, List
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime
import json
import re
import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name = "bilabonnement",
  api_key = "179299515168542",
  api_secret = "hQr86XL5c_RErMiffv5kf_eOy4c" ,
  secure = True
)


class Imove:
    def __init__(self):

        self.url = "https://imove.no/produkter"
        self.base = "https://imove.no"
        self.api = "https://imove.no/_next/data/fs72Ed8P4Z0-OYgdjeYs8/no/produkter.json"

    @classmethod
    def get_cars_api(cls) -> Dict:
        url = "https://imove.no/produkter"
        base = "https://imove.no"
        site = requests.get(url)
        soup = BS(site.text, "lxml")
        scripts = soup.select("script")
        script = [script.get("src") for script in scripts if "_buildMani" in script.get("src","")]
        datakey = script[0].split("/")[-2]
        api = f"https://imove.no/_next/data/{datakey}/no/produkter.json"
        
        data = requests.get(api).json()["pageProps"]["products"]
        cars = []
        with open("car.json") as file:
            template = json.load(file)
        for car in data:
            name = car["name"].lower().replace("Š".lower(),"s").capitalize()
            img = f"https://api.prod.imove.no/file/images/{car['images'][0]['imageId']}/raw?cloudinaryParams=w_480,h_302,c_fill,g_auto"
            cartemplate = template.copy()
            cartemplate.update(
                {
                    "site": "imove",
                    "name": name,
                    "make": car["name"].lower().replace("Š".lower(),"s").split()[0].capitalize(),
                    "model": "",
                    "content": [{"title": car.get("name",""), "byline": car.get("description")}],
                    "drive": "Elektrisk",
                    "extra": car.get("extra", []),
                    "battery": car.get("battery", ""),
                    "towbar": car.get("towbar", False),
                    "roofRack": car.get("roofRack", False),
                    "maxRoofLoad": car.get("maxRoofLoad", ""),
                    "power": car.get("power", ""),
                    "driveWheel": car.get("driveWheel", ""),
                    "year": car.get("productionYears",[])[0],
                    "seats": car.get("seats", [])[0],
                    "transmission": "auto",
                    "price":  car.get("price", ""),
                    "range": car.get("ranges", [])[-1],
                    "cargoVolume": car.get("cargoVolume", ""),
                    "kmMonth": "ubegrenset",
                    "location": ["Oslo","Bergen"],
                    "availability": "available",
                    "from": car.get("availableDates",[])[0].get("availableFrom",""),
                    "order": f"{url}/{car['slug']}",
                    "img": cloudinary.uploader.upload(img, folder="imove", overwrite=False, public_id=f"{name}{img.split('/')[-2]}")["secure_url"],
                    "cargoVolume": "",
                    }
            )
            cars.append(cartemplate)
        return (cars, )


    def get_links(self) -> List:
        response = requests.get(self.api)
        soup = BS(response.text, "lxml")
        cars = soup.findAll("article")
        links = [f"{self.base}{car.a['href']}" for car in cars]
        return links

    def get_car(self, url: str) -> Dict:
        matchstrig_sted = r"(?<=Tilgjengelig\s\si\s).*(?=fra)"
        matchstrig_dato = r"(?<=fra\s).*"
        response = requests.get(url)
        soup = BS(response.text, "lxml")
        car = {}
        try:
            car = {
                    "site": "imove",
                    "name": soup.find("h2", {"class": "Headers__H2-sc-156gim-1 lhuYdM"}).text,
                    "make": soup.find("h2", {"class": "Headers__H2-sc-156gim-1 lhuYdM"}).text.split()[0],
                    "model": "",
                    "drive": "Elektrisk",
                    "year": soup.select("li div p")[0].text,
                    "seats": soup.select("li div p")[3].text.replace(" seter",""),
                    "transmission": "auto",
                    "price":  "".join([match.group() for match in re.finditer("\d",soup.select(".guOFvB")[0].text)]),
                    "range": soup.select("li div p")[1].text.replace(" km rekkevidde",""),
                    "kmMonth": "ubegrenset km/måned",
                    "location": re.search(matchstrig_sted,soup.select("p.gSUBkT")[0].text).group().split(),
                    "availability": "available",
                    "from": re.search(matchstrig_dato,soup.select("p.gSUBkT")[0].text).group(),
                    "order": f'{url}',
                    "img": soup.find("img")["src"],
                    "cargoVolume": "",
                    }
        except Exception as E:
            print(E, url)
        return car


    def get_cars(self, postalcode=None):
        try:
            links = self.get_links()
            cars = []
            for link in links:
                cars.append(
                    self.get_car(link)
                )

            
            return (cars, )
        except Exception as e:
            print(e)
            return None
