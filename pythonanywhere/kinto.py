import requests
import json
import cloudinary
import cloudinary.uploader
from bs4 import BeautifulSoup as BS

cloudinary.config(
    cloud_name="bilabonnement",
    api_key="179299515168542",
    api_secret="hQr86XL5c_RErMiffv5kf_eOy4c",
    secure=True,
)


class Kinto:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        url = "https://www.kinto-flex.no/produkter"
        site = requests.get(url)
        soup = BS(site.text, "lxml")
        data = soup.select("#__NEXT_DATA__")
        data = json.loads(data[0].text)["props"]["pageProps"]["products"]
        cars = []
        with open("car.json") as file:
            template = json.load(file)
        for i, car in enumerate(data):
            try:
                name = car["name"].lower().replace("Š".lower(), "s").capitalize()
                img = f"https://api.prod.imove.no/file/images/{car['images'][0]['imageId']}/raw?cloudinaryParams=w_480,h_302,c_fill,g_auto"
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "kinto",
                        "name": name,
                        "make": car["name"]
                        .lower()
                        .replace("Š".lower(), "s")
                        .split()[0]
                        .capitalize(),
                        "model": "",
                        "content": [
                            {
                                "title": car.get("name", ""),
                                "byline": car.get("description"),
                            }
                        ],
                        "drive": "Hybrid"
                        if "hybrid" in car.get("vehicleTypes", [])[-1].lower()
                        else car.get("vehicleTypes", [])[-1]
                        .replace("Petrol", "bensin")
                        .replace("Phev", "hybrid")
                        .replace("Electric", "elektrisk"),
                        "extra": car.get("extra", []),
                        "battery": car.get("battery", ""),
                        "towbar": car.get("towbar", False),
                        "roofRack": car.get("roofRack", False),
                        "maxRoofLoad": car.get("maxRoofLoad", ""),
                        "power": car.get("power", ""),
                        "driveWheel": car.get("driveWheel", ""),
                        "year": car.get("productionYears", [])[0],
                        "seats": car.get("seats", [])[0],
                        "transmission": "auto",
                        "price": car.get("price", ""),
                        "range": car.get("ranges", [])[-1]
                        if car.get("ranges", [])
                        else "",
                        "cargoVolume": car.get("cargoVolume", ""),
                        "kmMonth": "1500",
                        "location": ["oslo", "bergen"],
                        "availability": "available",
                        "from": car.get("availableDates", [])[0].get(
                            "availableFrom", ""
                        )
                        if car.get("availableDates", [])
                        else "",
                        "order": f"{url}/{car['slug']}",
                        "img": cloudinary.uploader.upload(
                            img,
                            folder="kinto",
                            overwrite=False,
                            public_id=f"{name}{img.split('/')[-2]}",
                        )["secure_url"],
                    }
                )
                cars.append(cartemplate)
            except Exception as e:
                print(e, i)
        return (cars,)
