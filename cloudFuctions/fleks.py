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
            for car in cars["data"]:
                if(car["attributes"]["make"] == "PEU"):
                    car["attributes"]["make"] = "peugeot"
                if(car["attributes"]["make"] == "MER"):
                    car["attributes"]["make"] = "mercedes"
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
                        "location": ["Oslo"],
                        "availability": car["attributes"].get("availabilityStatus", ""),
                        "order": f"{base}{car['attributes'].get('slug','')}",
                        "img": car["attributes"].get("imageUrl", "")
                        
                    }
                )
                cleanCars.append(cartemplate)


            available = [car for car in cleanCars if car["availability"] == "available"]
            unavailable = [
                car for car in cleanCars if car["availability"] != "available"
            ]
            return (available, unavailable)
        except Exception as e:
            print(e)
            return None
