import requests

cache = {}
start_currency = input()

while True:

    response = requests.get(f" http://www.floatrates.com/daily/{start_currency}.json").json()
    # Immediately adds USD and EUR exchange rates to cache.
    if start_currency.lower() != 'usd':
        cache[response['usd']['code']] = float(response['usd']['rate'])
    if start_currency.lower() != 'eur':
        cache[response['eur']['code']] = float(response['eur']['rate'])

    exchange_currency = input().upper()

    if exchange_currency == "":
        break

    money_amount = float(input())

    print("Checking the cache...")
    if exchange_currency in cache:
        print("Oh! It is in the cache!")
        converted = round(money_amount * cache[exchange_currency], 2)
        print(f"You received {converted} {exchange_currency}.")
        continue
    else:
        print("Sorry, but it is not in the cache!")
        cache[response[exchange_currency.lower()]['code']] = float(response[exchange_currency.lower()]['rate'])
        converted = round(money_amount * cache[exchange_currency], 2)
        print(f"You received {converted} {exchange_currency}.")
        continue
