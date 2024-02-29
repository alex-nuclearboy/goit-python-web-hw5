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
    # Run the utility:
    $ python exchanger.py <number_of_days> [extra_currencies...]

`<number_of_days>`: The number of days to retrieve exchange rates for, up to a maximum of 10 days.
`[extra_currencies...]`: Optional. A space-separated list of additional currency codes to retrieve exchange rates for.

Example:

    python exchanger.py 2 PLN GBP

This command retrieves and displays the exchange rates for USD, EUR, PLN and GBP from the last 5 days.
