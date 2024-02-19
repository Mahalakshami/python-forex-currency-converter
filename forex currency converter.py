from forex_python.converter import CurrencyRates
import time

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("Enter the source currency code (e.g., USD): ").upper()
            to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

            converted_amount = convert_currency(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(2)  # Wait for 2 seconds before allowing another conversion

if __name__ == "__main__":
    main()
