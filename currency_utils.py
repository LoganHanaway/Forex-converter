import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = 'http://api.exchangerate.host/convert'
API_KEY = os.getenv('API_KEY')  # Get the API key from environment variables

def get_available_currencies():
    try:
        with open('currencies.json', 'r') as file:
            currencies = json.load(file)
        return currencies
    except FileNotFoundError:
        raise ValueError("Currency list file not found")
    except json.JSONDecodeError:
        raise ValueError("Error decoding currency list")

def convert_currency(from_currency, to_currency, amount):
    response = requests.get(API_URL, params={
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'access_key': API_KEY  # Use the API key from environment variables
    })
    data = response.json()
    if data.get('success'):
        return {'result': f"{data['result']:.2f} {to_currency}"}
    else:
        return {'error': data['error']}
