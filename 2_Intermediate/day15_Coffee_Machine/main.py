# Coffee Machine


from data import MENU, resources, coins
from tools import clear
from art import logo


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(choice):
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        return 1
    elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        return 2
    elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        return 3
    else:
        return 0


def process_coins():
    quarters = float(input("how many quarters?: ")) * coins["quarter"]
    dimes = float(input("how many dimes?: ")) * coins["dime"]
    nickles = float(input("how many nickles?: ")) * coins["nickel"]
    pennies = float(input("how many pennies?: ")) * coins["penny"]
    total = quarters + dimes + nickles + pennies
    return total


def make_coffee(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    resources["money"] += MENU[choice]["cost"]
    print(f"Here is your {choice} ☕️. Enjoy!")


clear()
print(logo)
next_customer = True
while next_customer is True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        report()
    elif user_choice == "off":
        next_customer = False
    else:
        if check_resources(choice=user_choice) == 1:
            print(f"Sorry there is not enough water.")
        elif check_resources(choice=user_choice) == 2:
            print(f"Sorry there is not enough milk.")
        elif check_resources(choice=user_choice) == 3:
            print(f"Sorry there is not enough coffee.")
        else:
            user_coins = round(process_coins(), 2)
            if user_coins < MENU[user_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif user_coins > MENU[user_choice]["cost"]:
                change = round(user_coins - MENU[user_choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                make_coffee(choice=user_choice)
            else:
                make_coffee(choice=user_choice)
