import requests


class Fleks:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        base = "https://app.fleks.no/bil/"
        api = "https://api.fleks.no/vehicletypes"
        response = requests.get(f"{api}")
        tries = 0
        while "20" not in str(response.status_code):
            response = requests.get(f"{api}", timeout=(2, 60))
            tries += 1
            if tries > 3:
                break
        cars = response.json()
        for car in cars["data"]:
            id = car["relationships"]["plans"]["data"][0]["id"]
            for i in cars["included"]:
                if i["type"] == "plans" and i["id"] == id:
                    price = i["attributes"]["price"]
            if len(str(price)) > 6:
                price = str(price)[:2] + str(price)[3:-1]
            else:
                price = str(price)[1] + str(price)[2:-1]
            car["attributes"]["price"] = price
        cleanCars = []
        for car in cars["data"]:
            cleanCars.append(
                {
                    "site": "fleks",
                    "name": car["attributes"]["modelDescription"],
                    "make": car["attributes"]["make"],
                    "model": car["attributes"]["model"],
                    "drive": car["attributes"]["transmission"],
                    "year": car["attributes"]["year"],
                    "seats": car["attributes"]["seats"],
                    "transmission": car["attributes"]["transmission"],
                    "price": car["attributes"]["transmission"],
                    "range": car["attributes"]["range"],
                    "location": ["Oslo"],
                    "availability": car["attributes"]["availabilityStatus"],
                    "order": f"{base}{car['attributes']['slug']}",
                    "img": car["attributes"]["imageUrl"],
                    "cargoVolume": car["attributes"]["cargoVolume"],
                }
            )

        available = [car for car in cleanCars if car["availability"] == "available"]
        unavailable = [car for car in cleanCars if car["availability"] != "available"]
        return (available, unavailable)
