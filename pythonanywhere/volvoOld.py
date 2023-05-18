import requests
import csv
import gzip
import json

import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="bilabonnement",
    api_key="179299515168542",
    api_secret="hQr86XL5c_RErMiffv5kf_eOy4c",
    secure=True,
)


class Volvo:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls):
        data = requests.get(
            "https://productdata.awin.com/datafeed/download/apikey/ceeddca9eb1a8117d71200c0fcd73db5/language/any/fid/83513,83515/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,merchant_id,category_name,category_id,aw_image_url,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,display_price,data_feed_id,brand_name,brand_id,colour,product_short_description,specifications,condition,product_model,model_number,dimensions,keywords,promotional_text,product_type,commission_group,merchant_product_category_path,merchant_product_second_category,merchant_product_third_category,rrp_price,saving,savings_percent,base_price,base_price_amount,base_price_text,product_price_old,delivery_restrictions,delivery_weight,warranty,terms_of_contract,delivery_time,in_stock,stock_quantity,valid_from,valid_to,is_for_sale,web_offer,pre_order,stock_status,size_stock_status,size_stock_amount,merchant_thumb_url,large_image,alternate_image,aw_thumb_url,alternate_image_two,alternate_image_three,alternate_image_four,reviews,average_rating,rating,number_available,custom_1,custom_2,custom_3,custom_4,custom_5,custom_6,custom_7,custom_8,custom_9,ean,isbn,upc,mpn,parent_product_id,product_GTIN,basket_link/format/csv/delimiter/%2C/compression/gzip/adultcontent/1/"
        )
        decompressed = gzip.decompress(data.content).decode("utf-8")

        reader = csv.DictReader(decompressed.splitlines(), delimiter=",")
        cars = [*reader]
        clean_cars = []
        for car in cars:
            try:
                img = car.get("merchant_image_url")

                with open("car.json") as file:
                    template = json.load(file)
                template.update({"site": "volvo"})
                template.update({"carid": car.get("aw_product_id")})
                template.update({"name": f"Volvo {car.get('product_name',{})}"})
                template.update({"make": "Volvo"})
                template.update({"model": car.get("model_number", {})})
                template.update({"content": ""})
                template.update(
                    {
                        "drive": car.get("specifications", {}).replace(
                            "Elektrisk/Bensin", "Hybrid"
                        )
                    }
                )
                template.update({"extra": ""})
                template.update({"battery": ""})
                template.update({"towbar": ""})
                template.update({"roofrack": ""})
                template.update({"maxRoofLoad": ""})
                template.update({"power": car.get("custom_1", {}).split("|")[1]})
                template.update({"driveWheel": car.get("custom_3", {})})
                template.update(
                    {
                        "seats": car.get("merchant_product_category_path", {}).replace(
                            " seter ", ""
                        )
                    }
                )
                template.update({"color": car.get("colour").replace("ö", "øn")})
                template.update({"transmission": car.get("custom_2")})
                template.update({"year": car.get("year")})
                template.update({"price": car.get("search_price")})
                template.update(
                    {"range": car.get("merchant_product_third_category", {})}
                )
                template.update(
                    {
                        "cargoVolume": car.get(
                            "merchant_product_second_category", {}
                        ).replace(" liter", "")
                    }
                )
                template.update(
                    {
                        "kmMonth": int(
                            float(cars[0].get("custom_9").replace(" km/md", ""))
                        )
                    }
                )
                template.update({"delivery": ""})
                template.update({"fuelconsumption": car.get("custom_4")})
                template.update({"co2": car.get("custom_5")})
                template.update({"engine": car.get("custom_1")})
                template.update({"engineDescription": ""})
                template.update({"type": car.get("product_type")})
                template.update({"binding": ""})
                template.update(
                    {"location": ["Oslo", "Bergen", "Trondheim", "Stavanger"]}
                )
                template.update({"availability": "available"})
                template.update({"order": car.get("merchant_deep_link")})
                template.update({"description": car.get("description")})
                template.update(
                    {
                        "img": cloudinary.uploader.upload(
                            img,
                            folder="volvo",
                            overwrite=False,
                            public_id=f'{template.get("carid")}',
                        )["secure_url"]
                    }
                )
                clean_cars.append(template)
            except Exception as e:
                print("Volvo failed to load car: ", car.get("aw_product_id"), e)
        return (clean_cars,)
