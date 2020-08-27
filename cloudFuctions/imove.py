import requests
from bs4 import BeautifulSoup as BS
import json


class Imove:
    def __init__(self):

        self.url = "https://secure.imove.no/cars"

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://secure.imove.no/cars"
            api = "https://secure.imove.no/api/vehicles"
            response = requests.get(f"{api}")
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}")
                tries += 1
                if tries > 3:
                    print("no response imove")
                    break
            if "20" not in str(response.status_code):
                return None
            cars = response.json()
            cleanCars = []
            for car in cars:
                cleanCars.append(
                    {
                        "site": "imove",
                        "name": f"{car['make']} {car['model']}",
                        "make": car["make"],
                        "model": car["model"],
                        "drive": "Elekrtisk"
                        if car["fuelType"] == "el"
                        else car["fuelType"],
                        "year": car["year"],
                        "seats": car["numberOfSeats"],
                        "transmission": "",
                        "price": int(car["pricePerMonth"]),
                        "range": car["range"],
                        "kmMonth": "",
                        "location": [
                            district["description"] for district in car["districts"]
                        ],
                        "availability": "available"
                        if car["isReserved"]
                        else "unavailable",
                        "order": f'{base}/{car["id"]}',
                        "img": f'{base}{car["images"][0]["url"]}'
                        if car["images"]
                        else "",
                        "cargoVolume": car["trunkCapacityInLiters"],
                    }
                )

            available = [car for car in cleanCars if car["availability"] == "available"]
            unavailable = [
                car for car in cleanCars if car["availability"] != "available"
            ]
            return (available, unavailable)
        except Exception as e:
            print(e)
            return None
