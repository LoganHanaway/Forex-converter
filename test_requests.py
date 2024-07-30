import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

from_currency = 'USD'
to_currency = 'EUR'
amount = 10

response = requests.get(
    f'http://api.exchangerate.host/convert',  # Use HTTP instead of HTTPS
    params={
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'access_key': API_KEY  # Include the API key in the request
    }
)
data = response.json()

print(f"Response Status Code: {response.status_code}")
print(f"Response Data: {data}")
