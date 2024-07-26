# MoneyUnify Python Client

The MoneyUnify Python Client is a package designed to simplify mobile money (MTN, Airtel, Zamtel) payments for businesses. It allows you to request payments, verify transaction statuses, and disburse funds using the MoneyUnify API.

## Installation

Install the package using pip:

```bash
pip install moneyunify
```

## Usage

### Initialize the Client

```python
from moneyunify import MoneyUnifyClient

client = MoneyUnifyClient(muid='your_moneyunify_id')
```

### Request Payment

```python
response = client.request_payment('0765655244', 5)
print(response)
```

### Verify Transaction

```python
response = client.verify_transaction('transaction_reference')
print(response)
```

### Send Money

```python
response = client.send_money('yourname@email.com', 'Iza', 'Sakir', '096xxxxxxx', 'Settle All funds from MoneyUnify')
print(response)
```
