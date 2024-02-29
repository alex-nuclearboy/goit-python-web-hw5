import aiohttp
import asyncio
import sys
from datetime import datetime, timedelta


class CurrencyExchangerPrivatBank:
    API_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="
    AVAILABLE_CURRENCIES = ['AUD', 'AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK',
                            'DKK', 'EUR', 'GBP', 'GEL', 'HUF', 'ILS', 'JPY',
                            'KZT', 'MDL', 'NOK', 'PLN', 'SEK', 'SGD', 'TMT',
                            'TRY', 'UAH', 'USD', 'UZS', 'XAU']

    def __init__(self, extra_currencies=None):
        """
        Initialize the object with a list of default currencies
        and extra currencies if provided.

        Parameters:
            extra_currencies (list): A list of extra currencies to be added
                                     to the default currencies.
                                     Defaults to None.
        """
        self.default_currencies = ['USD', 'EUR']
        if extra_currencies:
            self.currencies = self.default_currencies + [
                currency.upper() for currency in extra_currencies
                if currency.upper() in self.AVAILABLE_CURRENCIES]

            # Check for unknown currencies
            unknown_currencies = [
                currency for currency in extra_currencies
                if currency.upper() not in self.AVAILABLE_CURRENCIES]
            if unknown_currencies:
                print(
                    "Warning: Unknown currencies ignored: "
                    f"{', '.join(unknown_currencies)}")
        else:
            self.currencies = self.default_currencies

    async def get_currency_rates(self, session, date):
        """
        Asynchronously gets currency rates for a specific date.

        Parameters:
            session: The client session to be used for the HTTP request.
            date: The date for which the currency rates are to be retrieved.

        Returns:
            A dictionary containing the currency rates for the specified date.
        """
        formatted_date = date.strftime("%d.%m.%Y")
        try:
            async with session.get(self.API_URL + formatted_date) as response:
                response.raise_for_status()
                data = await response.json()
                rates = {currency: None for currency in self.currencies}
                for rate in data.get('exchangeRate', []):
                    if rate.get('currency') in self.currencies:
                        rates[rate.get('currency')] = {
                            'sale': rate.get('saleRate'),
                            'purchase': rate.get('purchaseRate')}
                return {formatted_date: rates}
        except aiohttp.ClientError as e:
            return {formatted_date: f"Failed to retrieve data: {str(e)}"}

    async def get_rates_for_days(self, days):
        """
        Retrieves exchange rates for the specified number of days.

        Parameters:
            days: The number of days for which to retrieve exchange rates.
        """
        if days > 10:
            print("Error: Exchange rates can only be retrieved for up to 10 days.")
            return

        async with aiohttp.ClientSession() as session:
            tasks = []
            for day_delta in range(days):
                date = datetime.now() - timedelta(days=day_delta)
                tasks.append(self.get_currency_rates(session, date))

            results = await asyncio.gather(*tasks)
            print(results)


def main():
    """
    The entry point for the program.
    It checks the command-line arguments for the number of days
    and additional currency codes, initializes the CurrencyExchangerPrivatBank
    class, and runs the asynchronous task to get currency exchange rates
    for the specified number of days.
    """
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: main.py <number_of_days> [additional_currencies...]")
        sys.exit(1)

    days = int(sys.argv[1])
    extra_currencies = (
        [currency.upper() for currency in sys.argv[2:]]
        if len(sys.argv) > 2 else None
    )
    currency_exchanger = CurrencyExchangerPrivatBank(extra_currencies)
    asyncio.run(currency_exchanger.get_rates_for_days(days))


if __name__ == "__main__":
    main()
