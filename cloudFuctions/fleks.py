import requests


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
                    price = str(price)[1] + str(price)[2:-1]
                car["attributes"]["price"] = price
            cleanCars = []
            translation = {
                "el": "Elektrisk",
                "petrol": "Bensin",
                "diesel": "Diesel",
                "petrol-hybrid": "Hybrid",
            }
            for car in cars["data"]:
                cleanCars.append(
                    {
                        "site": "fleks",
                        "name": car["attributes"]["modelDescription"],
                        "make": car["attributes"]["make"],
                        "model": car["attributes"]["model"],
                        "drive": translation[car["attributes"]["fuelType"]],
                        "year": car["attributes"]["year"],
                        "seats": car["attributes"]["seats"],
                        "transmission": car["attributes"]["transmission"],
                        "price": int(car["attributes"]["price"]),
                        "range": car["attributes"]["range"],
                        "kmMonth": "",
                        "location": ["Oslo"],
                        "availability": car["attributes"]["availabilityStatus"],
                        "order": f"{base}{car['attributes']['slug']}",
                        "img": car["attributes"]["imageUrl"],
                        "cargoVolume": car["attributes"]["cargoVolume"],
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
