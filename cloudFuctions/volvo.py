import requests
class Volvo:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls):
        try:
            api = "https://www.volvocars.com/api/care-by-volvo/cars/cars/?customerType=b2c&itemsPerPage=50&market=no&page=1"
            base = "https://www.volvocars.com/no/care-by-volvo/cars/"
            response = requests.get(api)
            while "20" not in str(response.status_code):
                response = requests.get(f"{api}", timeout=(2, 60))
                tries += 1
                if tries > 3:
                    print("no response volvo")
                    return None
            cars = response.json()["data"]
            cleanCars = []
            for car in cars:
                if car["listingType"] == "stock":
                    cleanCars.append(
                        {
                            "site": "volvo",
                            "name": car["title"],
                            "make": "Volvo",
                            "model": car["model"],
                            "drive": car["fuelType"],
                            "year": car["modelYear"],
                            "seats": car["numberOfSeats"],
                            "transmission": car["transmissionType"],
                            "price": car["basePrice"],
                            "range": car["electricRange"],
                            "location": ["Oslo","Bergen","Stavanger","Trondheim"],
                            "availability": "Available",
                            "order": f"{base}+{car['vehicleId']}",
                            "img": car["image"][0],
                            "cargoVolume": None
    }
                    )   
            
        except Exception as e:
            print(e)
            return None

        return cleanCars
