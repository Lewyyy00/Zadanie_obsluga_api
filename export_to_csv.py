import requests, json, csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates_list = data[0]['rates']

csv_file = "rates"
with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Zapisanie nagłówków
    csv_writer.writerow(['currency', 'code', 'bid', 'ask'])
    # Zapisanie danych 
    for rate in rates_list:
        csv_writer.writerow([rate['currency'], rate['code'], rate['bid'], rate['ask']])