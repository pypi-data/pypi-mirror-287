from datetime import timedelta

import requests
from ratelimit import limits, sleep_and_retry


class KinseyAPIClient:
    def __init__(self, base_url, access_token, skus):
        self.base_url = base_url
        self.access_token = access_token
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-API-TOKEN": f"{self.access_token}",
        }
        self.skus = skus

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def get_products(self, endpoint):
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}", headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None
