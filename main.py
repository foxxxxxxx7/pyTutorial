import requests


# Function to get exchange rates
def get_exchange_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Check if there was an error with the response data
        if data["result"] == "success":
            return data["conversion_rate"]
        else:
            print("Error fetching data. Please check currency codes.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Function to perform the currency conversion
def convert_currency(amount, from_currency, to_currency, api_key):
    rate = get_exchange_rate(from_currency, to_currency, api_key)
    if rate is not None:
        converted_amount = amount * rate
        print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency} at a rate of {rate}")
    else:
        print("Conversion failed due to an error fetching the exchange rate.")


def main():
    api_key = "your_exchangerate_api_key"  # Replace with your actual API key
    print("Welcome to the Currency Converter!")

    # Get user inputs
    from_currency = input("Enter the base currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    # Perform the conversion
    convert_currency(amount, from_currency, to_currency, api_key)


if __name__ == "__main__":
    main()
