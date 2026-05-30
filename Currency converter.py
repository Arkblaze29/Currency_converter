exchange_rate = {
        "SGD": 1,
        "MYR": 3.10,
        "THB": 25.54,
        "IDR": 13947,
        "PHP": 48.11,
        "VND": 20492,
        }

def converter(amount, from_currency, to_currency):
    converted_amount = round(amount * exchange_rate[to_currency] / exchange_rate[from_currency], 2)
    return f"{from_currency} {amount} is equal to {to_currency} {converted_amount}."

print("Hello! Welcome to Shang Wei's currency converter.")
print("Supported currencies are: SGD, MYR, THB, IDR, PHP, VND")
print("Please take note that the exchange rates are based on the market rates as of May 2026 and do not reflect actual exchange rates.")

while True:
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


