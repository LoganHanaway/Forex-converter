from flask import Flask, render_template, request, redirect, url_for
import currency_utils  # Ensure this imports correctly
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = request.form.get('amount')
        
        # Validate currencies and amount
        currencies = currency_utils.get_available_currencies()
        if from_currency not in currencies or to_currency not in currencies:
            return render_template('index.html', currencies=currencies, error="Invalid currency code")

        try:
            amount = float(amount)
        except ValueError:
            return render_template('index.html', currencies=currencies, error="Invalid amount")

        # Call the API to get conversion rate
        try:
            response = currency_utils.convert_currency(from_currency, to_currency, amount)
            if 'error' in response:
                return render_template('index.html', currencies=currencies, error=response['error']['info'])
            converted_amount = response['result']
            return render_template('index.html', currencies=currencies, converted_amount=converted_amount, from_currency=from_currency, to_currency=to_currency, amount=amount)
        except Exception as e:
            return render_template('index.html', currencies=currencies, error=str(e))
    
    # For GET request
    currencies = currency_utils.get_available_currencies()
    return render_template('index.html', currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
