from typing import Dict, List
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime
import json
import re
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="bilabonnement",
    api_key="179299515168542",
    api_secret="hQr86XL5c_RErMiffv5kf_eOy4c",
    secure=True,
)


class Hunsbedt:
    def __init__(self):

        pass

    @classmethod
    def get_cars(cls) -> Dict:
        url = "https://hunsbedt.no/bilutleie/"
        base = "https://hunsbedt.no/"
        site = requests.get(url)
        soup = BS(site.text, "lxml")
        data = soup.select(".uabb-blog-post-content")
        cars = []
        with open("car.json") as file:
            template = json.load(file)
        try:
            for car in data:
                name = car.select(".fl-heading-text")[0].text
                img = car.select("img.fl-photo-img")[0].get("src")
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "hunsbedt",
                        "name": name,
                        "make": car.select(".fl-heading-text")[0].text.split()[0],
                        "model": car.select(".fl-heading-text")[0].text.split()[1],
                        "content": [
                            {
                                "title": car.get("name", ""),
                                "byline": car.get("description"),
                            }
                        ],
                        "drive": car.select(
                            "div.fl-col.fl-node-602ea1cd8099d.fl-col-small > div > div > div > div > div.fl-callout-content > div > div > p:nth-child(1)"
                        )[0].text,
                        "extra": car.get("extra", []),
                        "battery": car.get("battery", ""),
                        "towbar": car.get("towbar", False),
                        "roofRack": car.get("roofRack", False),
                        "maxRoofLoad": car.get("maxRoofLoad", ""),
                        "power": car.get("power", ""),
                        "driveWheel": car.get("driveWheel", ""),
                        "year": car.get("productionYears", []),
                        "seats": car.get("seats", []),
                        "transmission": car.select(
                            ".fl-node-602ea1cd80998.fl-col-small > div > div > div > div > div.fl-callout-content > div > div > p:nth-child(1)"
                        )[0].text,
                        "price": car.select(
                            " div.fl-module.fl-module-rich-text.fl-node-603797e83470a > div > div > p"
                        )[0]
                        .text.replace("Langtidsleie pr mnd. ", "")
                        .replace(".", "")
                        .replace(",–", ""),
                        "range": car.get("ranges", []),
                        "cargoVolume": car.get("cargoVolume", ""),
                        "kmMonth": "3000",
                        "location": ["kvinesdal"],
                        "availability": "available",
                        "from": "",  # car.get("availableDates", [])[0].get("availableFrom", ""),
                        "order": "https://hunsbedt.no/bilutleie/",
                        "img": cloudinary.uploader.upload(
                            img,
                            folder="hunsbedt",
                            overwrite=False,
                            public_id=f"{name}{img.split('/')[-2]}",
                        )["secure_url"],
                        "cargoVolume": "",
                        "description": car.select(
                            "div > div.fl-module.fl-module-rich-text> div > div > p"
                        )[0].text,
                    }
                )
                cars.append(cartemplate)
        except Exception as e:
            print("Error hunsbedt ", e)
        return (cars,)
