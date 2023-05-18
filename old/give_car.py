import json
from functools import wraps
from typing import Any, Tuple

import config
from google.cloud import storage
from google.oauth2 import service_account


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
    blob.upload_from_string(str(data))


def load_tekst(client):
    tekst = load_from_cloud(client, config.text_blob_name, config.bucket_name)
    return json.loads(tekst)


def main(request, *args, **kwargs):

    SCOPES = ["https://www.googleapis.com/auth/devstorage.read_write"]
    CREDENTIALS = service_account.Credentials.from_service_account_file(
        config.cloud_credentials, scopes=SCOPES
    )
    BLOB_NAME = config.text_blob_name
    BUCKET_NAME = config.bucket_name
    client = storage.Client(project=config.bucket_name, credentials=CREDENTIALS)
    mycars = load_tekst(client)
    allowed_domains = [
        "http://localhost:8080",
        "http://localhost:8081",
        "https://bilabonnement.app",
        "https://bilabo.app",
        "https://test.bilabonnement.app",
    ]
    if request.environ["HTTP_ORIGIN"] in allowed_domains:
        origin = request.environ["HTTP_ORIGIN"]
    else:
        origin = "https://bilabonnement.app"

    headers = {
        "Access-Control-Allow-Origin": f"{origin}",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Max-Age": "3600",
    }
    return (json.dumps(mycars), 200, headers)
