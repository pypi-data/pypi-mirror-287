import unittest
from moneyunify import MoneyUnifyClient, ApiError, TimeoutError

class TestMoneyUnifyClient(unittest.TestCase):
    def setUp(self):
        self.client = MoneyUnifyClient(muid='test_muid')

    def test_request_payment(self):
        with self.assertRaises(ApiError):
            self.client.request_payment('invalid_phone', 10)

    def test_verify_transaction(self):
        with self.assertRaises(ApiError):
            self.client.verify_transaction('invalid_reference')

    def test_send_money(self):
        with self.assertRaises(ApiError):
            self.client.send_money('invalid_email', 'John', 'Doe', 'invalid_phone', 'details')

if __name__ == '__main__':
    unittest.main()
