# Pyexchange - Currency Exchange Console Application

## Overview

Pyexchange is a Python console application that leverages the exchangerate-api to provide accurate exchange rates. This project was created to gain hands-on experience in working with APIs and processing JSON data.

## Features

- Retrieve real-time exchange rate data for various currencies.
- Convert USD (United States Dollar) to other currencies based on the latest exchange rates.
- Store exchange rate data in a JSON file for offline use.
- User-friendly console interface.

## Getting Started

To use Pyexchange, follow these simple steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pyexchange.git

2. Install the required Python Libraries using pip:

    ```bash
    pip install requests

3. Run the application

    ```bash
    python pyexchange.py

## Usage

1. Upon running the application, it will fetch the latest exchange rate data from the exchangerate-api using USD as the base currency.

2. You will be prompted to enter the amount you'd like to convert (in USD) and the ISO code of the target currency (e.g., RUB for Russian Ruble).

3. The application will perform the conversion and display the result, showing both the input amount and the converted amount in the chosen currency.

4. You can choose to perform more conversions or exit the application.
