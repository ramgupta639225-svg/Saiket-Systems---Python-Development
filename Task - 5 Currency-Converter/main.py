import requests

API_URL = "https://api.frankfurter.dev/v2/rate"


def convert_currency():
    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        from_currency = input("Convert from (e.g. USD): ").strip().upper()
        to_currency = input("Convert to (e.g. INR): ").strip().upper()

        if len(from_currency) != 3 or len(to_currency) != 3:
            print("Please enter valid currency codes.")
            return

        if from_currency == to_currency:
            print(f"Converted amount: {amount:.2f} {to_currency}")
            return

        response = requests.get(
            f"{API_URL}/{from_currency}/{to_currency}",
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        rate = data["rate"]
        result = amount * rate

        print("\n===== CONVERSION RESULT =====")
        print(f"Exchange rate: 1 {from_currency} = {rate} {to_currency}")
        print(f"Converted amount: {result:.2f} {to_currency}")
        print(f"Rate date: {data.get('date', 'Not available')}")

    except ValueError:
        print("Please enter a valid amount.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.HTTPError:
        print("Currency not supported or rate not available.")

    except requests.exceptions.RequestException:
        print("Unable to connect to the currency API.")

    except (KeyError, TypeError):
        print("Invalid response received from the API.")


while True:
    print("\n===== CURRENCY CONVERTER =====")
    print("1. Convert Currency")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        convert_currency()

    elif choice == "2":
        print("Thank you for using Currency Converter!")
        break

    else:
        print("Invalid choice. Please select 1 or 2.")
