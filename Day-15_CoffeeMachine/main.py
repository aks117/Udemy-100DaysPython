from data import MENU, resources

machine_status = True

water = 0
milk = 0
coffee = 0
profit = 0.00


def initialize_resources():
    """Initializes all the resources needed for Coffee Machine."""
    global water, milk, coffee
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]


def check_resources(user_order):
    """Checks if the resources available are enough for the user's order."""
    global water, milk, coffee
    if water < user_order["water"]:
        return "Not enough water available for your order."
    elif milk < user_order["milk"]:
        return "Not enough milk available for your order."
    elif coffee < user_order["coffee"]:
        return "Not enough coffee available for your order."
    else:
        return "True"


def update_resources(user_order):
    """Updates the amount of resources available after a successful order."""
    global water, milk, coffee
    water -= user_order["water"]
    milk -= user_order["milk"]
    coffee -= user_order["coffee"]


def input_coins():
    """Asks the user to enter the coins to place an order."""
    quarters = int(input("How many quarters did you insert? \t"))
    dimes = int(input("How many dimes did you insert? \t"))
    nickel = int(input("How many nickels did you insert? \t"))
    penny = int(input("How many pennies did you insert? \t"))

    money_entered = (quarters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (penny * 0.01)

    return money_entered


def return_report():
    """Returns the report of resources available in the Coffee Machine."""
    global water, milk, coffee
    return f"Water : {water}\nMilk : {milk}\nCoffee : {coffee}\nProfit : {profit}"


def turn_off():
    """Turns the machine off."""
    global machine_status
    machine_status = False


def order(user_choice):
    """Takes order from a user choice."""
    global profit
    user_order = {}

    user_order["water"] = MENU[user_choice]["ingredients"]["water"]
    if not user_choice == "espresso":
        user_order["milk"] = MENU[user_choice]["ingredients"]["milk"]
    user_order["coffee"] = MENU[user_choice]["ingredients"]["coffee"]
    user_order["cost"] = MENU[user_choice]["cost"]

    if user_choice == "espresso":
        user_order["milk"] = 0

    is_resources_enough = check_resources(user_order)

    if is_resources_enough == "True":
        money_entered = input_coins()
        if money_entered < user_order["cost"]:
            print("That's not enough money.\nMoney Refunded.")
        else:
            update_resources(user_order)
            profit += user_order["cost"]
            change = money_entered - user_order["cost"]
            print(f"Here is your you change ${change}.")
            print(f"Here's your {user_choice}☕.\nEnjoy!")
    else:
        print(is_resources_enough)


def coffee_machine():
    """The main menu of the Coffee Machine."""
    user_choice = input("What would you like to have? (Espresso / Latte / Cappuccino)\nEnter a command : \t").lower()
    if user_choice == "report":
        print(return_report())
    elif user_choice == "off":
        turn_off()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        order(user_choice)
    else:
        print("Invalid Input.\t")


if __name__ == "__main__":
    initialize_resources()
    while machine_status:
        coffee_machine()

