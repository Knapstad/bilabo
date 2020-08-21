import requests


class Flex:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        api = "https://api.fleks.no/vehicletypes"
        response = requests.get(f"{api}")
        tries = 0
        while "20" not in response:
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
            if len(str(price))> 6:
                price = str(price)[:2] + str(price)[3:-1]
            else:
                price = str(price)[1] + str(price)[2:-1]
            car["attributes"]["price"] = price
        available = [
            car["attributes"]
            for car in cars["data"]
            if car["attributes"]["availabilityStatus"] == "available"
        ]
        unavailable = [
            car["attributes"]
            for car in cars["data"]
            if car["attributes"]["availabilityStatus"] != "available"
        ]
        return (available, unavailable)

