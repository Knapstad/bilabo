import requests
from Bot import Bot
from bs4 import BeautifulSoup as BS
import json


class Imove:
    def __init__(self):

        self.url = "https://secure.imove.no/cars"

    @classmethod
    def get_cars(cls, postalcode=None):
        headers = {"User-Agent": "My User Agent 1.0"}
        base = "https://secure.imove.no/cars"
        api = "https://secure.imove.no/api/vehicles"
        response = requests.get(f"{api}", headers=headers)
        tries = 0
        while "20" not in str(response.status_code):
            response = requests.get(f"{api}")
            tries += 1
            if tries > 3:
                break
        if "20" not in str(response.status_code):
            print("no response")
            print(response)
            print(response.text)
        cars = response.json()
        cleanCars = []
        for car in cars:
            cleanCars.append(
                {
                    "name": f"{car['make']} {car['model']}",
                    "make": car["make"],
                    "model": car["model"],
                    "drive": car["fuelType"],
                    "year": car["year"],
                    "seats": car["numberOfSeats"],
                    "transmission": "",
                    "price": car["pricePerMonth"],
                    "range": car["range"],
                    "location": [
                        district["description"] for district in car["districts"]
                    ],
                    "availability": "available" if car["isReserved"] else "unavailable",
                    "order": f'{base}{car["id"]}',
                    "img": f'{base}{car["images"][0]["url"]}' if car["images"] else "",
                    "cargoVolume": car["trunkCapacityInLiters"],
                }
            )

        available = [car for car in cleanCars if car["availability"] == "available"]
        unavailable = [car for car in cleanCars if car["availability"] != "available"]
        return (available, unavailable)

