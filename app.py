from flask import Flask, render_template, request

app = Flask(__name__)

conversion_rates = {
    'usd': 	3.9859,
    'eur': 	4.3514,
    'gbp': 	5.0169
}

@app.route('/calulator', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        amount = float(request.form['amount'])
        currency = request.form['currency']

        if not amount or not currency:
            result = "Invalid input"
        elif currency not in conversion_rates:
            result = "Invalid currency"
        else:
            result = amount * conversion_rates[currency]

    return render_template('szablon.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)