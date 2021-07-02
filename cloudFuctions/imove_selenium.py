import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime
import json


class Imove:
    def __init__(self):

        self.url = "https://imove.no/produkter"
        self.base = "https://imove.no"
        self.api = "https://imove.no/produkter"


    def get_links(self):
        response = requests.get(self.api)
        soup = BS(response.text, "lxml")
        cars = soup.findAll("article")
        links = [f"{self.base}{car.a['href']}" for car in cars]
        return links

    def get_cars(self, postalcode=None):
        
        try:
            
            
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
                        "drive": "Elektrisk"
                        if car["fuelType"] == "el"
                        else car["fuelType"],
                        "year": car["year"],
                        "seats": car["numberOfSeats"],
                        "transmission": "auto",
                        "price": int(car["pricePerMonth"]),
                        "range": car["range"],
                        "kmMonth": "ubegrenset km/måned",
                        "location": [
                            district["description"] for district in car["districts"]
                        ],
                        "availability": "available"
                        if not car["isReserved"]
                        else "unavailable",
                        "from": car["availableFromDate"],
                        "order": f'{base}/{car["id"]}',
                        "img": f"https://secure.imove.no{car['images'][0]['url']}" if car["images"] else "svg",
                        "cargoVolume": car["trunkCapacityInLiters"],
                    }
                )

            available = [
                car
                for car in cleanCars
                if car["availability"] == "available"
                and (datetime.now() - datetime.fromisoformat(car["from"][:-1])).days
                < 15
            ]
            unavailable = [
                car for car in cleanCars if car["availability"] != "available"
            ]
            return (available, unavailable)
        except Exception as e:
            print(e)
            return None
