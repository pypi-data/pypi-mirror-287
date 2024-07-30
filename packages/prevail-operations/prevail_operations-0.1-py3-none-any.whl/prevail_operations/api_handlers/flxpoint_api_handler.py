## Contains classes or functions for authentication, making API requests, and handling responses.
## Handles endpoint-specific functionalities (e.g., orders, inventory, pricing).

from datetime import timedelta

import requests
from ratelimit import limits, sleep_and_retry


class FlxpointAPIClient:
    def __init__(
        self, base_url, access_token, page, per_page, start_date, skus, status, tags
    ):
        self.base_url = base_url
        self.access_token = access_token
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-API-TOKEN": f"{self.access_token}",
        }
        self.page = page
        self.per_page = per_page
        self.start_date = start_date
        self.skus = skus
        self.status = status
        self.tags = tags

    @property
    def data(self):
        return {
            "page": f"{self.page}",
            "per_page": f"{self.per_page}",
            "orderedAfter": f"{self.start_date}",
        }

    @property
    def orderStatus(self):
        if self.status:
            return "&status=" + f"{self.status}"
        return

    @property
    def includeTags(self):
        if self.tags:
            return "&includeTags=" + f"{self.tags}"
        return

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def create_return(self, endpoint, data):
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}", headers=self.headers, json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def update_inventory_variants(self, endpoint, data):
        try:
            response = requests.put(
                f"{self.base_url}/{endpoint}", headers=self.headers, json=data
            )
            response.raise_for_status()
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def get_orders(self, endpoint):
        try:
            # print(self.data)
            if self.page:
                page = "?page=" + str(self.page)
            else:
                page = ""

            if self.per_page:
                per_page = "&pageSize=" + str(self.per_page)
            else:
                per_page = ""

            if self.start_date:
                start_date = "&orderedAfter=" + str(self.start_date)
            else:
                start_date = ""

            if self.orderStatus:
                orderStatus = self.orderStatus
            else:
                orderStatus = ""

            if self.includeTags:
                includeTags = self.includeTags
            else:
                includeTags = ""

            base_url = f"{self.base_url}/{endpoint}"
            url = f"{base_url}{str(page)}{str(per_page)}{str(start_date)}{orderStatus}{includeTags}"

            # print(url)

            response = requests.get(
                url,
                headers=self.headers,
            )
            response.raise_for_status()
            # print(response.json)
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def update_order_status(self, endpoint, order_id):
        try:
            response = requests.patch(
                f"{self.base_url}/{endpoint}{order_id}/status?status=Open",
                headers=self.headers,
            )
            response.raise_for_status
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def update_return_status(self, endpoint, return_id, data):
        try:
            response = requests.patch(
                f"{self.base_url}/{endpoint}{return_id}",
                headers=self.headers,
                json=data,
            )
            response.raise_for_status
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def get_product_variants(self, endpoint, data):
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                params=data,
            )
            response.raise_for_status
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def update_product_variants(self, endpoint, data):
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                json=data,
            )
            response.raise_for_status
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None

    @sleep_and_retry
    @limits(calls=2, period=timedelta(seconds=1).total_seconds())
    def update_source_variants(self, endpoint, data):
        try:
            response = requests.put(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                json=data,
            )
            response.raise_for_status
            return response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Error occurred: {err}")
            return None
