import json
import logging


from swap import Swap
from fleks import Fleks
from imove import Imove
from kinto import Kinto
from volvo import Volvo
from sesong import Sesong
from hunsbedt import Hunsbedt
from flexidrive import Flexidrive
from enterprise import Enterprise


def main(*args, **kwargs):

    try:
        logging.warning("running Fleks")
        fleks = Fleks.get_cars()
    except Exception as e:
        logging.warning(f"fleks: {e}")
        fleks = []

    try:
        logging.warning("running Imove")
        imove = Imove.get_cars_api()
    except Exception as e:
        logging.warning(f"Imove: {e}")
        imove=[]

    try:
        logging.warning("running Swap")
        swap = Swap.get_cars()
    except Exception as e:
        logging.warning(f"swap: {e}")
        swap = []
    try:
        logging.warning("running Kinto")
        kinto = Kinto.get_cars()
    except Exception as e:
        logging.warning(f"kinto: {e}")
        kinto=[]

    try:
        logging.warning("running Volvo")
        volvo = Volvo.get_cars()
    except Exception as e:
        logging.warning(f"Volvo: {e}")
        volvo = []

    try:
        logging.warning("running Flexidrive")
        flexidrive = Flexidrive.get_cars()
    except Exception as e:
        logging.warning(f"Flexidrive {e}")
        flexidrive = []

    try:
        logging.warning("running Enterprise")
        enterprise = Enterprise.get_cars()
    except Exception as e:
        logging.warning(f"Enterprise {e}")
        enterprise = []

    try:
        logging.warning("running Sesong")
        sesong = Sesong.get_cars()
    except Exception as e:
        logging.warning(f"Sesong {e}")
        sesong = []

    try:
        logging.warning("running Hunsbedt")
        hunsbedt = Hunsbedt.get_cars()
    except Exception as e:
        logging.warning(f"Hunsbedt {e}")
        hunsbedt = []


    with open("mysite/mycars.json","r") as f:
        mycars = json.load(f)

    if fleks:
        mycars["fleks"] = fleks[0]
    else:
        logging.warning("fleks empty")
    if imove:
        mycars["imove"] = imove[0]
    else:
        logging.warning("imove empty")
    if swap:
        mycars["swap"] = swap[0]
    else:
        logging.warning("swap empty")
    if sesong:
        mycars["sesongbil"] = sesong[0]
    else:
        logging.warning("sesong empty")
    if kinto:
        mycars["kinto"] = kinto[0]
    else:
        logging.warning("kinto empty")
    if volvo:
        mycars["volvo"]=volvo[0]
    else:
        logging.warning("volvo empty")
        mycars["volvo"] = []
    if flexidrive:
        mycars["flexidrive"] = flexidrive[0]
    else:
        logging.warning("flexidrive empty")
    if enterprise:
        mycars["enterprise"] = enterprise[0]
    else:
        logging.warning("enterprise empty")
    if hunsbedt:
        mycars["hunsbedt"] = hunsbedt[0]
    else:
        logging.warning("hunsbedt empty")

    siteid = {}
    for site in mycars:
        for car in mycars[site]:
            car["id"]=f"{siteid.get(car['site'],1)}{site[0]}{site[-1]}"
            siteid[site] = siteid.get(site,1)+1

    with open("mysite/mycars.json","w") as f:
        mycars = json.dump(mycars, f)
    logging.warning("Done!")

if __name__ == "__main__":
    main()
