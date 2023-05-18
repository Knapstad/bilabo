import requests
import json
import cloudinary
import cloudinary.uploader
from bs4 import BeautifulSoup as BS

cloudinary.config(
  cloud_name = "bilabonnement",
  api_key = "179299515168542",
  api_secret = "hQr86XL5c_RErMiffv5kf_eOy4c" ,
  secure = True
)

class Sesong:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://sesongbil.no"
            api = "https://www.sesongbil.no/velg-bil/"
            response = requests.get(f"{api}")
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response flex")
                    return None
            template = json.load(open("car.json"))
            soup = BS(response.text, "lxml")
            locations = soup.select(".car-loc")
            clean_cars = ([],)
            for loc in locations:
                location = [loc.attrs["data-location"].replace("sentrum","").replace("lesund","ålesund")]
                cars = loc.select(".car-wrapper")
                for car in cars:
                    clean_car = template.copy()
                    clean_car["name"] = car.h3.text
                    clean_car["make"] = car.h3.text.split()[0]
                    clean_car["model"] = " ".join(car.h3.text.split()[1:])
                    clean_car["drive"] = car.select(".fuel")[0].next_sibling.text
                    clean_car["doors"] = car.select(".doors")[0].next_sibling.text
                    clean_car["transmission"] = car.select(".gear")[0].next_sibling.text
                    clean_car["seats"] = car.select(".seats")[0].next_sibling.text
                    clean_car["cargoVolume"] = car.select(".luggage")[0].next_sibling.text
                    clean_car["towbar"] = car.select(".hook")[0].next_sibling.text == "Ja"
                    clean_car["co2"] = car.select(".co2")[0].next_sibling.text
                    clean_car["site"] = "sesongbil"
                    clean_car["description"] = car.select(".desc")[0].text
                    clean_car["price"] = car.select(".prisen")[0].text.replace(",-","")
                    clean_car["kmMonth"] = 1500
                    clean_car["order"] = f"{base}{car.select('.bestill-bil')[0].attrs['action']}"
                    clean_car["details"] = {}
                    details = BS(requests.get(clean_car["order"]).text, "lxml")
                    img = f'{base}{details.select("img")[0].attrs["src"]}'
                    extra = details.select("ul.accordion li")
                    for i in extra:
                        clean_car["details"][i.h3.text]=i.p.text
                    clean_car["year"] = details.select(".post-header")[0].text.split()[-1]
                    clean_car["location"] = location
                    clean_car["img"] = cloudinary.uploader.upload(img, folder="sesong", overwrite=False, public_id=f"{clean_car['name']}{img.split('/')[-2]}")["secure_url"]
                    clean_cars[0].append(clean_car)
            return clean_cars
        except Exception as e:
            print(e)
            return None
