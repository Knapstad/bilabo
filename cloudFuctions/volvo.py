class Volvo:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls):

        cars = [
            {
                "name": "Volvo xc90 Recharge",
                "make": "Volvo",
                "model": "XC90 Recharge",
                "drive": "Hybrid",
                "year": 2020,
                "seats": 7,
                "transmission": "Automat",
                "price": 11990,
                "range": 50,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/suv/xc90?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/256/exterior-v1/R7/49200/R14D/2G03/_/LR02/TC05/TP05/_/_/SR02/TM04/GR02/T101/TJ02/NP03/_/JG02/CB03/EV02/JB06/T214/LF05/_/VP03/_/FH01/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
            {
                "name": "Volvo xc60 Recharge",
                "make": "Volvo",
                "model": "XC60 Recharge",
                "drive": "Hybrid",
                "year": 2020,
                "seats": 5,
                "transmission": "Automat",
                "price": 10990,
                "range": 53,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/suv/xc60?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/536/exterior-v1/R6/72800/R171/FN02/_/TC06/TP05/LR02/JT02/GR08/T101/TJ02/TM04/JG02/CB04/_/JB0C/T21A/LF05/_/_/_/_/_/_/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
            {
                "name": "Volvo xc40 Recharge Pure electric",
                "make": "Volvo",
                "model": "XC40 Recharge Pure electric",
                "drive": "Elektrisk",
                "year": 2020,
                "seats": 5,
                "transmission": "Automat",
                "price": 7990,
                "range": 400,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/suv/xc40?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/536/exterior-v1/R6/72800/R171/FN02/_/TC06/TP05/LR02/JT02/GR08/T101/TJ02/TM04/JG02/CB04/_/JB0C/T21A/LF05/_/_/_/_/_/_/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
            {
                "name": "Volvo s90 Recharge",
                "make": "Volvo",
                "model": "S90 Recharge ",
                "drive": "Hybrid",
                "year": 2020,
                "seats": 5,
                "transmission": "Automat",
                "price": 9990,
                "range": None,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/sedan/s90?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/234/exterior-v1/R5/73100/RB0R00/R15C/_/TC05/LR02/TM04/GR02/T101/NP02/JG02/JB0A/T214/LF05/_/VP03/CB03/_/EV03/_/_/PU02/FH01/2G03/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
            {
                "name": "Volvo v90 Recharge",
                "make": "Volvo",
                "model": "V90 Recharge ",
                "drive": "Hybrid",
                "year": 2020,
                "seats": 5,
                "transmission": "Automat",
                "price": 9990,
                "range": None,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/stasjonsvogn/v90?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/235/exterior-v1/R5/73100/RB0R00/R15C/_/TC05/TP05/LR02/_/TM04/GR02/T101/JG02/JB0A/T214/LF05/_/VP03/FH01/CB03/_/EV02/_/_/PU02/2G03/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
            {
                "name": "Volvo s60 Recharge",
                "make": "Volvo",
                "model": "S60 Recharge ",
                "drive": "Hybrid",
                "year": 2020,
                "seats": 5,
                "transmission": "Automat",
                "price": 8990,
                "range": None,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/sedan/s60?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/224/exterior-v1/R5/71400/R133/_/_/TM04/_/SR02/_/T101/JB0C/T214/CB03/_/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
            {
                "name": "Volvo v60 Recharge",
                "make": "Volvo",
                "model": "v60 Recharge ",
                "drive": "Hybrid",
                "year": 2020,
                "seats": 5,
                "transmission": "Automat",
                "price": 8990,
                "range": None,
                "location": ["Oslo", "Bergen", "Stavanger"],
                "availability": "available",
                "order": "https://www.volvocars.com/no/build/stasjonsvogn/v60?filter=carebyvolvo&customerType=b2c&ref=cbv-b2c",
                "img": "https://cas.volvocars.com/image/dynamic/MY21_2017/225/exterior-v1/R5/71400/R133/TP05/LR02/TM04/_/SR02/_/T101/JB0C/T214/CB03/_/_/SideModelpage.jpg?market=no&client=vbsgw&Angle=7&bg=ffffff&w=600",
                "cargoVolume": "",
            },
        ]
        return cars
