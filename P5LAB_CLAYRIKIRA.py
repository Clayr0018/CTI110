# Rikira Clay
# April 20, 2025
# P5LAB – Self-Checkout Change Dispenser
# This program simulates a self-checkout machine that calculates how much change
# to return to a customer using dollars, quarters, dimes, nickels, and pennies.

import random  # Module import for generating random amount owed

# Function to break down change into denominations
def disperse_change(change):
    cents = round(change * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    print("Change breakdown:")
    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)

# Main program logic
def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print("Amount owed: $", total_owed)

    # Loop until valid amount of cash is entered
    while True:
        try:
            cash = float(input("Enter amount of cash given: $"))
            if cash >= total_owed:
                break
            else:
                print("Not enough money. Please enter an amount equal to or greater than the amount owed.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    change = round(cash - total_owed, 2)
    print("Change owed: $", change)

    disperse_change(change)

# Run the program
main()
