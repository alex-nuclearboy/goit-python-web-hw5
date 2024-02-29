import aiohttp
import asyncio
import sys
from datetime import datetime, timedelta


class CurrencyExchangerPrivatBank:
    API_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="
    AVAILABLE_CURRENCIES = ['USD', 'EUR', 'GBP', 'PLN', 'CAD', 'JPY', 'CHF', 'SEK', 'XAU', 'UAH']

    def __init__(self, extra_currencies=None):
        self.default_currencies = ['USD', 'EUR']
        if extra_currencies:
            self.currencies = self.default_currencies + [currency.upper() for currency in extra_currencies if currency.upper() in self.AVAILABLE_CURRENCIES]
            # Check for unknown currencies
            unknown_currencies = [currency for currency in extra_currencies if currency.upper() not in self.AVAILABLE_CURRENCIES]
            if unknown_currencies:
                print(f"Warning: Unknown currencies ignored: {', '.join(unknown_currencies)}")
        else:
            self.currencies = self.default_currencies

    async def get_currency_rates(self, session, date):
        formatted_date = date.strftime("%d.%m.%Y")
        try:
            async with session.get(self.API_URL + formatted_date) as response:
                response.raise_for_status()
                data = await response.json()
                rates = {currency: None for currency in self.currencies}
                for rate in data.get('exchangeRate', []):
                    if rate.get('currency') in self.currencies:
                        rates[rate.get('currency')] = {'sale': rate.get('saleRate'), 'purchase': rate.get('purchaseRate')}
                return {formatted_date: rates}
        except aiohttp.ClientError as e:
            return {formatted_date: f"Failed to retrieve data: {str(e)}"}

    async def get_rates_for_days(self, days):
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
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: main.py <number_of_days> [additional_currency_codes...]")
        sys.exit(1)

    days = int(sys.argv[1])
    extra_currencies = [currency.upper() for currency in sys.argv[2:]] if len(sys.argv) > 2 else None
    currency_exchanger = CurrencyExchangerPrivatBank(extra_currencies)
    asyncio.run(currency_exchanger.get_rates_for_days(days))


if __name__ == "__main__":
    main()
