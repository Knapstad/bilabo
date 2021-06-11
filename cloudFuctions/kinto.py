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
            for car in cars:
                cleanCars.append(
                    {
                        "site": "kinto",
                        "name": f"{car.get('make','')} {car.get('model','')}",
                        "make": car.get("make", ""),
                        "model": car.get("model", ""),
                        "drive": "",
                        "year": car.get("year", ""),
                        "seats": car.get("seats", ""),
                        "transmission": car.get("transmission", ""),
                        "price": int(car.get("pricePerMonth", "")),
                        "range": car.get("range", ""),
                        "kmMonth": "",
                        "location": ["Oslo"],
                        "availability": car.get("available", False),
                        "order": f"{base}/car/{car.get('id','')}",
                        "img": f"{base}{car.get('image', '')}",
                        "cargoVolume": car.get("cargoVolume", ""),
                    }
                )

            available = [car for car in cleanCars if car.get("availability", 0)]
            unavailable = [car for car in cleanCars if not car.get("availability", 0)]
            return (available, unavailable)
        except Exception as e:
            print(e)
            return None
