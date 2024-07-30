from datetime import timedelta

import requests
from ratelimit import limits, sleep_and_retry


class TopdawgAPIClient(object):
    def __init__(self, base_url, access_token, page, per_page, startDate):
        self.base_url = base_url
        self.access_token = access_token
        self.page = page
        self.per_page = per_page
        self.headers = {"Authorization": f"{self.access_token}"}
        self.startDate = startDate

    @property
    def data(self):
        return {
            "page": f"{self.page}",
            "per_page": f"{self.per_page}",
            "created_from": f"{self.startDate}",
        }

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @sleep_and_retry
    @limits(calls=600, period=timedelta(seconds=60).total_seconds())
    def get_orders(self, endpoint):
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}", headers=self.headers, data=self.data
            )
            response.raise_for_status()
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"HTTP error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=5, period=timedelta(seconds=10).total_seconds())
    def get_products(self, endpoint, updated_at_date):
        try:
            data = self.data

            if updated_at_date != 0:
                data["product_updated_at"] = updated_at_date

            response = requests.post(
                f"{self.base_url}/{endpoint}", headers=self.headers, data=data
            )
            response.raise_for_status()
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"HTTP error occurred: {err}")
            return None
