
import requests
from decimal import Decimal, InvalidOperation

API_URL = "https://api.frankfurter.dev/v2/rate"

def convert_currency():
    try:
        amount = Decimal(input("Enter amount: ").strip())

        if not amount.is_finite() or amount < 0:
            print("Please enter a valid non-negative amount!")
            return

        from_currency = input("Convert from (e.g. USD): ").strip().upper()
        to_currency = input("Convert to (e.g. INR): ").strip().upper()

        if (len(from_currency) != 3 or not from_currency.isalpha()
                or len(to_currency) != 3 or not to_currency.isalpha()):
            print("Please enter valid three-letter currency codes!")
            return

        if from_currency == to_currency:
            print(f"{amount} {from_currency} = {amount:.2f} {to_currency}")
            return

        response = requests.get(
            f"{API_URL}/{from_currency}/{to_currency}",
            timeout=15
        )
        response.raise_for_status()

        data = response.json()
        rate = Decimal(str(data["rate"]))
        result = amount * rate

        print("\n========== CONVERSION RESULT ==========")
        print(f"Exchange rate: 1 {from_currency} = {rate} {to_currency}")
        print(f"Converted amount: {result:.2f} {to_currency}")
        print(f"Rate date: {data.get('date', 'Not provided')}")

    except InvalidOperation:
        print("Please enter a valid numeric amount!")

    except requests.exceptions.HTTPError:
        print("Currency not supported or rate not available.")

    except requests.exceptions.RequestException as error:
        print(f"API connection error: {error}")

    except (KeyError, ValueError):
        print("Invalid response received from the API.")


while True:
    print("\n========== CURRENCY CONVERTER ==========")
    print("1. Convert Currency")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        convert_currency()

    elif choice == "2":
        print("Thank you for using Currency Converter!")
        break

    else:
        print("Invalid choice!")
