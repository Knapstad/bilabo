import requests
import json
import cloudinary
import cloudinary.uploader
import re

cloudinary.config( 
  cloud_name = "bilabonnement", 
  api_key = "179299515168542", 
  api_secret = "hQr86XL5c_RErMiffv5kf_eOy4c" ,
  secure = True
)

class Fleks:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://app.fleks.no/bil/"
            api = "https://api.fleks.no/vehicletypes"
            response = requests.get(f"{api}")
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response flex")
                    return None
            cars = response.json()
            for car in cars["data"]:
                id = car["relationships"]["plans"]["data"][0]["id"]
                for i in cars["included"]:
                    if i["type"] == "plans" and i["id"] == id:
                        price = i["attributes"]["price"]
                if len(str(price)) > 6:
                    price = str(price)[:2] + str(price)[3:-1]
                else:
                    price = str(price)[0] + str(price)[2:-1]
                car["attributes"]["price"] = price
            cleanCars = []
            with open("car.json") as file:
                template = json.load(file)
            translation = {
                "el": "Elektrisk",
                "petrol": "Bensin",
                "diesel": "Diesel",
                "petrol-hybrid": "Hybrid",
            }
            match = "[^a-zA-Z0-9\n\.]"
            for car in cars["data"]:
                if(car["attributes"]["make"] == "PEU"):
                    car["attributes"]["make"] = "peugeot"
                if(car["attributes"]["make"] == "MER"):
                    car["attributes"]["make"] = "mercedes"
                public_id = f'{car["attributes"].get("modelDescription","")}{car["attributes"].get("imageUrl", "").split("/")[-1].split(".")[0]}'
                public_id = re.sub(match,'',public_id)
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "fleks",
                        "name": car["attributes"].get("modelDescription",""),
                        "make": car["attributes"].get("make", ""),
                        "model": car["attributes"].get("model",""),
                        "content": car["attributes"].get("content", ""),
                        "drive": translation[car["attributes"].get("fuelType", "")],
                        "extra": car["attributes"].get("specifications",[]),
                        "battery": car["attributes"].get("battery",""),
                        "towbar": car["attributes"].get("towbar",""),
                        "roofRack": car["attributes"].get("roofRack",""),
                        "maxRoofLoad": car["attributes"].get("maxRoofLoad",""),
                        "power": car["attributes"].get("power",""),
                        "driveWheel": car["attributes"].get("driveWheel",""),
                        "seats": car["attributes"].get("seats", ""),
                        "transmission": car["attributes"].get("transmission", ""),
                        "price": int(car["attributes"].get("price", "")),
                        "range": car["attributes"].get("range", ""),
                        "cargoVolume": car["attributes"].get("cargoVolume", ""),
                        "kmMonth": "1000",
                        "location": ["oslo"],
                        "availability": car["attributes"].get("availabilityStatus", ""),
                        "order": f"{base}{car['attributes'].get('slug','')}",
                        "img": cloudinary.uploader.upload(car["attributes"].get("imageUrl", ""), folder="fleks", overwrite=False, public_id=public_id)["secure_url"]
                        
                    }
                )
                cleanCars.append(cartemplate)


            available = [car for car in cleanCars if car["availability"] != "unavailable"]
            unavailable = [
                car for car in cleanCars if car["availability"] == "unavailable"
            ]
            return (available, unavailable)
        except Exception as e:
            print(e)
            return None
