import json
import math
from functools import wraps
from typing import Any, Tuple
import logging

from google.auth import credentials
import config

from swap import Swap
from fleks import Fleks
from imove import Imove
from kinto import Kinto
from volvo import Volvo
from flexidrive import Flexidrive
from enterprise import Enterprise

from google.cloud import storage
from google.oauth2 import service_account
import google.cloud.logging

SCOPES = ["https://www.googleapis.com/auth/devstorage.read_write"]
CREDENTIALS = service_account.Credentials.from_service_account_file(
    config.cloud_credentials, scopes=SCOPES
    )


client = google.cloud.logging.Client(credentials=CREDENTIALS)
client.get_default_handler()
client.setup_logging()


def retry_on_connection_error(max_retry: int = 3):
    def decorate_function(function):
        @wraps(function)
        def retry(*args, **kwargs):
            tries = 0
            while tries < max_retry:
                try:
                    return function(*args, **kwargs)
                except ConnectionError:
                    tries += 1
            return function(*args, **kwargs)

        return retry

    return decorate_function


@retry_on_connection_error()
def load_from_cloud(
    client: "google.cloud.storage.client.Client", blob_name: str, bucket_name: str
):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    return blob.download_as_string()


@retry_on_connection_error()
def save_to_cloud(
    client: "google.cloud.storage.client.Client",
    data: Any,
    blob_name: str,
    bucket_name: str,
):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    if not blob:
        blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data))


def load_tekst(client):
    tekst = load_from_cloud(client, config.blob_name, config.bucket_name)
    return json.loads(tekst)


def main(*args, **kwargs):

    SCOPES = ["https://www.googleapis.com/auth/devstorage.read_write"]
    CREDENTIALS = service_account.Credentials.from_service_account_file(
        config.cloud_credentials, scopes=SCOPES
    )

    BLOB_NAME = config.blob_name
    BUCKET_NAME = config.bucket_name

    client = storage.Client(project=config.bucket_name, credentials=CREDENTIALS)

    fleks = Fleks.get_cars()
    imove = Imove.get_cars_api()
    swap = Swap.get_cars()
    kinto = Kinto.get_cars()
    volvo = Volvo.get_cars()
    flexidrive = Flexidrive.get_cars()
    enterprise = Enterprise.get_cars()
    mycars = load_tekst(client)
    
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
    if kinto:
        mycars["kinto"] = kinto[0]
    else:
        logging.warning("kinto empty")
    if volvo:
        mycars["volvo"]=volvo[0]
    else:
        logging.warning("volvo empty")
    if flexidrive:
        mycars["flexidrive"] = flexidrive[0]
    if enterprise:
        mycars["enterprise"] = enterprise[0]
    else:
        logging.warning("enterprise empty")

    save_to_cloud(client, mycars, BLOB_NAME, BUCKET_NAME)


if __name__ == "__main__":
    pass
