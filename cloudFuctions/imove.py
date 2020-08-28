import requests
from bs4 import BeautifulSoup as BS
import json


class Imove:
    def __init__(self):

        self.url = "https://secure.imove.no/cars"

    @classmethod
    def get_cars(cls, postalcode=None):
        images = {
            "BMW  i3 120ah": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW  i3 Charged Plus": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW  i3 Fully Charged": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW I3 120 Ah ": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW I3 94 Ah": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 120 Ah": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 120Ah": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 120Ah Fully Charged (SPZ)": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 94 Ah": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 94Ah": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 94Ah (SPZ)": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 Charged": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 Charged Plus": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 Charged plus": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 Fully Charged": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3 Fully Charged ": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "BMW i3s 94Ah (SPZ)": "BMW__i3_Charged_Plus_wyat3q.jpg",
            "DS 3 Crossback (SPZ)": "DS_3_Crossback_l8skwa.jpg",
            "Honda e": "Honda_e_isqmvv.png",
            "Honda e (SPZ)": "Honda_e_isqmvv.png",
            "Hyundai Ioniq EV": "hundai_ionic_mmw0o2.png",
            "Hyundai Ioniq EV ": "hundai_ionic_mmw0o2.png",
            "Hyundai Kona 64 kw (SPZ)": "Hyunda_kona_pypdwt.jpg",
            "Hyundai Kona 64kW (SPZ)": "Hyunda_kona_pypdwt.jpg",
            "KIA e-Soul 64 kw (SPZ)": "KIA_e-Soul_lsakit.jpg",
            "Kia E-Niro (SPZ)": "kia-niro_u7cgdl.png",
            "Kia Soul Active 30kW": "KIA_e-Soul_lsakit.jpg",
            "Kia Soul EV ": "KIA_e-Soul_lsakit.jpg",
            "Kia Soul Exclusive": "KIA_e-Soul_lsakit.jpg",
            "Kia e-Soul 64 kw (SPZ)": "KIA_e-Soul_lsakit.jpg",
            "MG ZS EV Comfort": "mg_ZS_xrbefp.png",
            "MG ZS EV Comfort ": "mg_ZS_xrbefp.png",
            "MG ZS EV Luxury": "mg_ZS_xrbefp.png",
            "MG ZS EV Luxury ": "mg_ZS_xrbefp.png",
            "MG ZS EV Luxury (SPZ)": "mg_ZS_xrbefp.png",
            "MG ZS EV Luxury (SPZ) ": "mg_ZS_xrbefp.png",
            "Nissan Leaf ": "nissan_leaf_m4rmmc.jpg",
            "Nissan Leaf 40 kw (SPZ)": "nissan_leaf_m4rmmc.jpg",
            "Nissan Leaf 62kW (SPZ)": "nissan_leaf_m4rmmc.jpg",
            "Nissan Leaf Tekna 40 kw (SPZ) ": "nissan_leaf_m4rmmc.jpg",
            "Nissan Leaf Tekna 62kW (SPZ)": "nissan_leaf_m4rmmc.jpg",
            "Nissan e-NV200 ": "Nissan_e-NV200_zcp5hr.jpg",
            "Peugeot e-2008": "Peugeot_e-208_ic0bnm.jpg",
            "Peugeot e-208": "Peugeot_e-2008_vhluhb.jpg",
            "Polestar 2": "Polestar_2_q7glmo.jpg",
            "SEAT Mii Electric": "SEAT_Mii_Electric_xuewhc.png",
            "Seat Mii Electric": "SEAT_Mii_Electric_xuewhc.png",
            "Seat Mii Electric ": "SEAT_Mii_Electric_xuewhc.png",
            "Seat Mii Electric (SPZ)": "SEAT_Mii_Electric_xuewhc.png",
            "Skoda CITIGOe IV": "Skoda_CITIGOe_ierjzq.ong",
            "Skoda Citigo (SPZ)": "Skoda_CITIGOe_ierjzq.ong",
            "Tesla  Model S 75D": "Tesla__Model_S_rjksdm.png",
            "Tesla Model 3 Long Range": "Tesla-Model-E_adwpvb.png",
            "Tesla Model 3 Preformance": "Tesla_-Model-X_sehhta.png",
            "Tesla Model X 75D": "Tesla_-Model-X_sehhta.png",
            "Volksvagen e-Up": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen E-Up! Range": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen e-Golf": "Volkswagen_e-Golf_w2qhce.jpg",
            "Volkswagen e-Golf ": "Volkswagen_e-Golf_w2qhce.jpg",
            "Volkswagen e-Golf (SPZ)": "Volkswagen_e-Golf_w2qhce.jpg",
            "Volkswagen e-UP! Range": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen e-Up": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen e-Up ": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen e-Up!": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen e-Up! ": "Volkswagen_e-Up_tnrdho.png",
            "Volkswagen e-Up! Range": "Volkswagen_e-Up_tnrdho.png",
        }
        try:
            img_url = (
                "https://res.cloudinary.com/db0kzjtgs/image/upload/v1598602983/imove/"
            )
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
                if f"{car['make']} {car['model']}" in images:
                    img = img_url + images[f"{car['make']} {car['model']}"]
                else:
                    img = "svg"
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
                        "img": img,
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
