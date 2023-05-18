import requests
import json

import cloudinary
import cloudinary.uploader

cloudinary.config( 
  cloud_name = "db0kzjtgs", 
  api_key = "327478757255189", 
  api_secret = "nYe7sbLMsViWWntcMuQuOkCoStI",
  secure = True
)

class Volvo:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls):
        try:
            api = "https://www.volvocars.com/api/care-by-volvo/cars/cars/?customerType=b2c&itemsPerPage=50&market=no&page=1"
            base1 = "https://www.volvocars.com"
            base2 = "https://www.volvocars.com/no/care-by-volvo/cars/"
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
                try:
                    extradata = requests.get(f"{apibase}{car.get('vehicleId')}/?market=no&customerType=b2c")
                    extradata = extradata.json().get("data",{})
                    name = f"Volvo {car.get('title')}"
                    img = car.get("image")
                    thiscar = template.copy()
                    if car.get("listingType") == "stock":
                        thiscar.update(
                            {"order": f"{base2}/{car.get('vehicleId')}"}
                        )
                    else:
                        thiscar.update(
                            {"order": f"{base1}{car.get('linkUrl')}"}
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
                            "name": name,
                            "make": "Volvo",
                            "model": car.get("model"),
                            "drive": car.get("fuelType").replace("PureElectric","Elektrisk"),
                            "year": car.get("modelYear"),
                            "seats": car.get("numberOfSeats"),
                            "transmission": car.get("transmissionType"),
                            "price": car.get("basePrice"),
                            "range": car.get("electricRange"),
                            "location": ["oslo","bergen","stavanger","trondheim"],
                            "availability": "Available",
                            "kmMonth": int(car.get("baseMonthlyMileage")),
                            "delivery": car.get("deliveryTime") ,
                            "fuelconsumption": car.get("fuelConsumption") ,
                            "towbar": car.get("hasTowbar"),
                            "co2": car.get("co2"),
                            "binding": "3md oppsigelse eller 36mnd binding" if car.get("fuelType")=="PureElectric" else "3mnd oppsigelse",
                            "order": f"{base1}{car.get('linkUrl')}",
                            # "img": cloudinary.uploader.upload(img, folder="volvo", overwrite=False, public_id=f'{name}{img.split("/")[-1].replace(".jpg?","").replace("&","")}')["secure_url"],
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
        except Exception as e:
            print(e)


        return (cleanCars, )
