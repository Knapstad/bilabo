import requests
import json
class Volvo:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls):
        try:
            api = "https://www.volvocars.com/api/care-by-volvo/cars/cars/?customerType=b2c&itemsPerPage=50&market=no&page=1"
            base = "https://www.volvocars.com/no/care-by-volvo/cars"
            base1 = "https://www.volvocars.com"
            apibase= "https://www.volvocars.com/api/care-by-volvo/cars/cars/"
            response = requests.get(api)
            tries = 0
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response volvo")
                    return None
            cars = response.json()["data"]
            cleanCars = []
            with open("car.json") as file:
                template = json.load(file)
            for car in cars:
                if car.get("listingType") == "stock":
                    extradata = requests.get(f"{apibase}{car['vehicleId']}/?market=no&customerType=b2c")
                    extradata = extradata.json()["data"]
                    thiscar = template.copy()
                    if car.get("listingType") == "stock":
                        thiscar.update(
                            "order": f"{base}/{car.get('vehicleId')}"
                        )
                    else:
                        thiscar.update(
                            "order": "order": f"{base1}{car.get('linkUrl')}"
                        )
                    thiscar.update(
                        {
                            "site": "volvo",
                            "horsePower": extradata.get("horsePower"),
                            "accelleration": extradata.get("acceleration"),
                            "categories": extradata.get("categories"),
                            "packages": extradata.get("packages"),
                            "options": extradata.get("options"),
                            "offers": extradata.get("offers"),
                            "name": f"Volvo {car.get('title')}",
                            "make": "Volvo",
                            "model": car.get("model"),
                            "drive": car.get("fuelType").replace("PureElectric","Elektrisk"),
                            "year": car.get("modelYear"),
                            "seats": car.get("numberOfSeats"),
                            "transmission": car.get("transmissionType"),
                            "price": car.get("basePrice"),
                            "range": car.get("electricRange"),
                            "location": ["Oslo","Bergen","Stavanger","Trondheim"],
                            "availability": "Available",
                            "kmMonth": int(car.get("baseMonthlyMileage")),
                            "delivery": car.get("deliveryTime") ,
                            "fuelconsumption": car.get("fuelConsumption") ,
                            "towbar": car.get("hasTowbar"),
                            "co2": car.get("co2"),
                            "binding": "3md oppsigelse eller 36mnd binding" if car.get("fuelType")=="PureElectric" else "3mnd oppsigelse",
                            "order": f"{base}/{car.get('vehicleId')}",
                            "img": car.get("image"),
                            "cargoVolume": car.get("cargoCapacity"),
                            "engine": car.get("engine"),
                            "enginDescription": car.get("engineDescription"),
                            "type": car.get("modelType"),
                            "color": car.get("color"),
                            "paint": car.get("paint")
                        }
                    )
                    cleanCars.append(thiscar)

        except Exception as e:
            print(e)
            return None

        return (cleanCars, )
