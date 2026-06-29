import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

BASE_CURRENCY = "SGD"
SUPPORTED_CURRENCIES = ("SGD", "MYR", "THB", "IDR", "PHP", "VND")
EXCHANGE_RATE_API_URL = f"https://open.er-api.com/v6/latest/{BASE_CURRENCY}"

exchange_rate = {
    "SGD": 1.0,
    "MYR": 3.10,
    "THB": 25.54,
    "IDR": 13947,
    "PHP": 48.11,
    "VND": 20492,
}


def refresh_exchange_rates():
    with urlopen(EXCHANGE_RATE_API_URL, timeout=8) as response:
        payload = json.load(response)

    if payload.get("result") != "success":
        raise ValueError("Exchange rate API returned a non-success result.")

    rates = payload["rates"]
    missing_currencies = [currency for currency in SUPPORTED_CURRENCIES if currency not in rates]
    if missing_currencies:
        raise KeyError(
            f"Exchange rate API response is missing currencies: {', '.join(missing_currencies)}."
        )

    return {currency: float(rates[currency]) for currency in SUPPORTED_CURRENCIES}

def converter(amount, from_currency, to_currency):
    converted_amount = round(amount * exchange_rate[to_currency] / exchange_rate[from_currency], 2)
    return f"{from_currency} {amount} is equal to {to_currency} {converted_amount}."

print("Hello! Welcome to Shang Wei's currency converter.")
print("Supported currencies are: SGD, MYR, THB, IDR, PHP, VND")
print("Live exchange rates are fetched from open.er-api.com before each conversion.")

while True:
    try:
        exchange_rate = refresh_exchange_rates()
    except (URLError, HTTPError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Unable to refresh live rates right now. Using the last available rates. Details: {error}")

    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            if amount < 0:
                print("Invalid input, amount cannot be negative, please try again.")
            else:
                break
        except ValueError:
            print("Invalid input, please enter a valid number.")
    
    while True:
        from_currency = input("Enter the currency you want to convert from:").upper()
        if from_currency not in exchange_rate:
            print("Invalid input, please enter a supported currency:")
        else:
            break  
    
    while True:
        to_currency = input("Enter the currency you want to convert to:").upper()
        if to_currency not in exchange_rate:
            print("Invalid input, please enter a supported currency:")
        else:
            break  
    
    result = converter(amount, from_currency, to_currency)
    print(result)
    
    convert_again = input("Do you want to convert another amount?\nEnter Yes to continue or No to exit:").lower()
    if convert_again != 'yes' and convert_again != 'no':
        convert_again = input("Invalid input, please enter Yes or No:").lower()
    elif convert_again == 'no':
        print("Thank you for using the currency converter. Goodbye!")
        break
    else:
        continue

