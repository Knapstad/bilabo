import requests
import re
import json


class Kinto:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://www.kinto.no"
            api = "https://www.kinto.no/cars/all"
            response = requests.get(f"{api}")
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response flex")
                    return None
            html = response.text
            pattern = r"({\"dataManager\".*?)<\/script"
            data = json.loads(re.search(pattern, response.text).group(1))
            cars = data["query"]["cars"]

            cleanCars = []
            with open("car.json") as file:
                template = json.load(file)
            for car in cars:
                if "hydrogen" in car.get("model",""):
                            drive =  "hydrogen"
                elif "electric" in car.get("model",""):
                    drive = "elekrisk"
                else:
                    drive = "bensin"
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "kinto",
                        "name": f"{car.get('make','')} {car.get('model','')}",
                        "make": car.get("make", ""),
                        "model": car.get("model", ""),
                        "drive": drive,
                        "year": car.get("year", ""),
                        "seats": car.get("seats", ""),
                        "transmission": car.get("transmission", ""),
                        "price": int(car.get("pricePerMonth", "")),
                        "range": car.get("range", ""),
                        "kmMonth": "1500",
                        "location": ["Oslo"],
                        "availability": car.get("available", False),
                        "order": f"{base}/car/{car.get('id','')}",
                        "img": f"{base}{car.get('image', '')}",
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
