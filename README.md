# Pyexchange - Currency Exchange Application

## Overview

Pyexchange is a Python application that leverages the exchangerate-api to provide accurate exchange rates. This project was created to gain hands-on experience in working with APIs, processing JSON data, and creating desktop application GUIs with Qt for Python(PySide6).

## Features

- Retrieve real-time exchange rate data for various currencies.
- Convert USD (United States Dollar) to other currencies based on the latest exchange rates.
- Store exchange rate data in a JSON file for offline use.
- User-friendly console interface.
- User-friendly GUI made using Qt for Python(PySide6)

## Getting Started

Make sure you already have pip and python installed on your system: 
https://www.python.org/downloads/
https://pip.pypa.io/en/stable/installation/

To use Pyexchange, follow these simple steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/WillieDLive/Pyexchange.git

2. Install the required Python Libraries using pip (You don't need pyside6 if you only want to use the console version):

    ```bash
    pip install requests
    pip install pyside6

3. Navigate to the source code:

    ```bash
    cd Pyexchange/

4. Run the Application

   Console version
   ```bash
    python src/pyexchange.py
   ```
   GUI version
   ```bash
   python src/main.py

## Usage

Console Version
1. Upon running the application, it will fetch the latest exchange rate data from the exchangerate-api using USD as the base currency.

2. You will be prompted to enter the amount you'd like to convert (in USD) and the ISO code of the target currency (e.g., RUB for Russian Ruble).

3. The application will perform the conversion and display the result, showing both the input amount and the converted amount in the chosen currency.

4. You can choose to perform more conversions or exit the application.

GUI Version
1. Upon runnin the application, it will fetch the latest exchange rate data from the exchangerate-api using USD as the base currency.

2. You will see a label saying "Enter USD Amount:" simply enter the amount (in USD) you want to convert. Then select a currency from the dropbox below it.

3. Click the "Convert!" button to see your converted amount.
