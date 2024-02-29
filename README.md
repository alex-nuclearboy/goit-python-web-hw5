# Currency Exchange Rates Checker for PrivatBank

This utility is a simple console application that retrieves and displays the currency exchange rates from PrivatBank for a specified number of days, up to a maximum of the last 10 days. It leverages the public API of PrivatBank, which maintains an archive of currency exchange rates data for the last 4 years.

## Features

- **Asynchronous API Calls:** Uses `aiohttp` for non-blocking network requests to fetch exchange rates efficiently.
- **Flexible Date Range:** Users can specify the number of days to retrieve exchange rates for, with a limit of up to 10 days to prevent excessive data retrieval.
- **Error Handling:** Implements error handling to manage network-related errors.
- **Support for Multiple Currencies:** While primarily focused on EUR and USD, the utility is designed to easily extend support for additional currencies.

## Requirements

- `Python 3`
- `aiohttp`
- `asyncio`

## Installation and Usage

    # Clone this repository to the local machine:
    $ git clone https://github.com/alex-nuclearboy/goit-python-web-hw5.git
    # Navigate to the cloned repository directory:
    $ cd goit-python-web-hw5
    # Install the required Python packages:
    $ pip install aiohttp

This utility offers several modes of operation depending on the provided command-line arguments. Below are the ways you can use this utility:

- Running the utility without any parameters retrieves the exchange rates for USD and EUR for today

        python exchanger.py

- Specifying a number as the only parameter retrieves the exchange rates for USD and EUR for the number of days specified, up to 10 days.

        python exchanger.py <number_of_days>

- Providing one or more currency codes as parameters retrieves the exchange rates for USD, EUR, and the specified additional currencies for today. Only supported currencies will be considered.

        python exchanger.py <currency_codes...>

- Specifying a number followed by one or more currency codes retrieves the exchange rates for USD, EUR, and the specified additional currencies for the number of days specified, up to 10 days.

        python exchanger.py <number_of_days> <currency_codes...>

Example:

    python exchanger.py 3 PLN GBP

This command retrieves and displays the exchange rates for USD, EUR, PLN and GBP from the last 3 days.

## Supported Currency Codes

The utility supports a wide range of currency codes, including AUD, AZN, BYN, CAD, CHF, CNY, CZK, DKK, EUR, GBP, GEL, HUF, ILS, JPY, KZT, MDL, NOK, PLN, SEK, SGD, TMT, TRY, UAH, USD, UZS, and XAU. 

**NOTE:**  For some of these currencies, PrivatBank exchange rates may not be available on certain days.