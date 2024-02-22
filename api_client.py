"""
Make requests to the API
"""

import requests


class APIClient:
    """
    Make API requests to the free, public FakeStoreAPI
    """

    API_HOST_URL = "https://fakestoreapi.com"

    def __init__(self) -> None:
        self.headers = {}

    def update_headers(self, content_type: dict[str, str]) -> None:
        """
        Updates the request headers

        Args:
            content_type (dict[str, str,]): An example of this would be {"Content-Type": "application/json", "Accept": "application/json"}
        """
        self.headers = content_type

    def get_products(self):
        """
        GET all products from the FakeStoreAPI
        """
        self.update_headers(
            content_type={
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

        resp = requests.get(
            url=f"{APIClient.API_HOST_URL}/products", headers=self.headers
        )
        resp.raise_for_status()

        return resp.json()

    def get_product_by_id(self, product_id: str):
        """
        GET a single product by its ID

        Args:
            product_id (str): ID of the product to GET from the API
        """
        self.update_headers(
            content_type={
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

        resp = requests.get(
            url=f"{APIClient.API_HOST_URL}/products/{product_id}", headers=self.headers
        )
        resp.raise_for_status()

        return resp.json()

    def get_product_by_category(self, product_category: str):
        """
        GET products in a single category

        Args:
            product_category (str): category to filter products on
        """
        self.update_headers(
            content_type={
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

        resp = requests.get(
            url=f"{APIClient.API_HOST_URL}/products/category/{product_category}",
            headers=self.headers,
        )
        resp.raise_for_status()

        return resp.json()
