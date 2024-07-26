import requests
from requests.exceptions import HTTPError, Timeout

class ApiError(Exception):
    pass

class TimeoutError(Exception):
    pass

class MoneyUnifyClient:
    BASE_URL = "https://api.moneyunify.com/v2"
    TIMEOUT = 10

    def __init__(self, muid):
        self.muid = muid

    def request_payment(self, phone_number, amount):
        url = f"{self.BASE_URL}/request_payment"
        data = {
            'muid': self.muid,
            'phone_number': phone_number,
            'amount': amount
        }
        try:
            response = requests.post(url, data=data, timeout=self.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            raise ApiError(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            raise TimeoutError(f"Request timed out: {timeout_err}")
        except Exception as err:
            raise ApiError(f"Other error occurred: {err}")

    def verify_transaction(self, reference):
        url = f"{self.BASE_URL}/verify_transaction"
        data = {
            'muid': self.muid,
            'reference': reference
        }
        try:
            response = requests.post(url, data=data, timeout=self.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            raise ApiError(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            raise TimeoutError(f"Request timed out: {timeout_err}")
        except Exception as err:
            raise ApiError(f"Other error occurred: {err}")

    def send_money(self, email, first_name, last_name, phone_number, transaction_details):
        url = f"{self.BASE_URL}/send_money"
        data = {
            'muid': self.muid,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'transaction_details': transaction_details
        }
        try:
            response = requests.post(url, data=data, timeout=self.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            raise ApiError(f"HTTP error occurred: {http_err}")
        except Timeout as timeout_err:
            raise TimeoutError(f"Request timed out: {timeout_err}")
        except Exception as err:
            raise ApiError(f"Other error occurred: {err}")
