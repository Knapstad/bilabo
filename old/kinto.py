from selenium import webdriver
import json
from bs4 import BeautifulSoup as BS

class Kinto:
    def __init__(self):
        pass

    @classmethod
    def get_cars(cls, postalcode=None):
        try:
            base = "https://www.kinto.no"
            api = "https://www.kinto.no/produkter"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            browser = webdriver.Chrome(options=chrome_options)
            browser.get(api)
            browser.find_element_by_css_selector(".LinkButton-sc-140e6lz-0").click()
            links = [link.get_attribute("href") for link in browser.find_elements_by_class_name("ivbups") if "produkter/" in link.get_attribute("href")]
            cleanCars = []
            with open("car.json") as file:
                template = json.load(file)
            for link in links:
                browser.get(link)
                extra_keys = browser.find_elements_by_css_selector(".gXQitm")
                for i in extra_keys:
                    browser.execute_script("arguments[0].click();", i)
                extra_keys= [key.text for key in extra_keys]
                extra_values = [value.text for value in browser.find_elements_by_css_selector("#accordion__panel-raa-0")]
                extradict = dict(zip(extra_keys, extra_values))
                cartemplate = template.copy()
                cartemplate.update(
                    {
                        "site": "kinto",
                        "name": browser.find_element_by_css_selector("div.Box-sc-1ld0et1-0.Flex-sc-2sde10-0.kqoHdf.bILvfu > h2").text,
                        "make": browser.find_element_by_css_selector("div.Box-sc-1ld0et1-0.Flex-sc-2sde10-0.kqoHdf.bILvfu > h2").text.split(" ")[0],
                        "model": " ".join(browser.find_element_by_css_selector("div.Box-sc-1ld0et1-0.Flex-sc-2sde10-0.kqoHdf.bILvfu > h2").text.split(" ")[1:-1]),
                        "drive": browser.find_element_by_css_selector(".src__CordSvg-sc-1fn61nl-16").find_element_by_xpath("./../..").text.split("\n")[-1].replace(" (Bensin)","").replace(" (Diesel)",""),
                        "year": browser.find_element_by_css_selector(".src__CalendarSvg-sc-1fn61nl-13").find_element_by_xpath("../..").text.split("\n")[-1],
                        "seats": browser.find_element_by_css_selector(".src__ManSvg-sc-1fn61nl-15").find_element_by_xpath("./../..").text.split("\n")[-1].split(" ")[0],
                        "transmission":"automat",
                        "price": int(browser.find_element_by_css_selector("#__next > main > div.Box-sc-1ld0et1-0.cQMKvc > div > section > div.Box-sc-1ld0et1-0.Flex-sc-2sde10-0.BarContainer-uhiasd-0.jZCGHd.bILvfu.guGAjd > div > section > div > div > div.Box-sc-1ld0et1-0.Flex-sc-2sde10-0.kqoHdf.bILvfu > div > p.Text-ng0wsq-0.cbJnND").text.replace(" ","").replace("kr/mnd","")),
                        "range": "",
                        "kmMonth": "1500",
                        "location": ["Oslo"],
                        "availability": "avaiable",
                        "order": link,
                        "img": browser.find_element_by_css_selector("img").get_attribute("src"),
                        "cargoVolume": "",
                        "description": browser.find_element_by_css_selector("div.Box-sc-1ld0et1-0.ixXCJs > p").text,
                        "details": extradict

                        }
                )
                cleanCars.append(cartemplate)

            available = [car for car in cleanCars if car.get("availability", 0)]
            unavailable = [car for car in cleanCars if not car.get("availability", 0)]
            return (available, unavailable)
        except Exception as e:
            print(e, link)
            return None
