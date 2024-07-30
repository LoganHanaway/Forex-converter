import unittest
from app import app
from currency_utils import validate_amount, get_conversion_rate

class CurrencyConverterTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_convert_valid(self):
        response = self.app.post('/convert', data=dict(from_currency='USD', to_currency='EUR', amount='10'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('converted_amount', response.get_json())

    def test_convert_invalid_amount(self):
        response = self.app.post('/convert', data=dict(from_currency='USD', to_currency='EUR', amount='abc'))
        self.assertEqual(response.status_code, 400)

    def test_convert_invalid_currency(self):
        response = self.app.post('/convert', data=dict(from_currency='XXX', to_currency='EUR', amount='10'))
        self.assertEqual(response.status_code, 400)

    def test_validate_amount(self):
        self.assertEqual(validate_amount('10'), 10.0)
        with self.assertRaises(ValueError):
            validate_amount('abc')

    def test_get_conversion_rate(self):
        rate = get_conversion_rate('USD', 'USD', 1)
        self.assertEqual(rate, 1.0)

if __name__ == '__main__':
    unittest.main()
