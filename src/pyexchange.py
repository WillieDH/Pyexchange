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

# Loops the lookup and conversion functionality
global active
active = True
while active:
    # Prompt User for their USD values to be converted and iso code
    print('---------------------------------------------------------\nEnter the amount you\'d like to convert (USD): ')
    usd_value = float(input())
    print('---------------------------------------------------------\nEnter conversion iso code (ex. RUB): ')
    user_iso_code = input()

    # Loops through iso_codes
    for iso_code, conv_rate in file_data_dict['conversion_rates'].items():
        # if iso_code is Russion Ruble
        if iso_code.lower() == user_iso_code.lower():
            # multiply by conversion rate
            converted_value = usd_value * (conv_rate)
            print(usd_value, 'USD = ', converted_value, iso_code)
    
    # Promt User to convert again
    print('---------------------------------------------------------\nDo you want to do another conversion? Y/n')
    user_continue = input()
    if user_continue.lower() == 'y':
        continue
    elif user_continue.lower() == 'n':
        active = False
    else:
        print('Sorry that\'s not a valid option. I\'ll just assume you want to close the program. Thank You! :)')
        active = False


