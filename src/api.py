import requests # library for API functionality
import json # library for putting data into the data file

# API link from exchangerate-api using USD as the base currency
url = 'https://v6.exchangerate-api.com/v6/c49f063f3e1fc9d1bb57a783/latest/USD'

# Make a request for the data
response = requests.get(url)
data = response.json()

# Place json data from API request into /data
with open('data\exchange_rates.json', 'w') as file:
    json.dump(data, file)

# Takes json data and puts it into variable
with open('data\exchange_rates.json', 'r') as file_read:
    file_data = file_read.read()

# Turns json data into python dictionary
file_data_dict = json.loads(file_data)