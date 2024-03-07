from menu import MENU

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

beverage_list = [beverage for beverage in MENU]


# ---------------------------- STEP 1: TAKING THE ORDER ------------------------------- #


def taking_order():
    machine_on = True
    while machine_on:
        making_beverage = True    # To use it to skip the step of making beverages if the money entered is not enough.
        order = input("What would you like? (espresso, latte, cappuccino) or type 'report': ").lower()

        # To print the available stock.
        if order == "report":
            print(f"Water: {stock["water"]}ml\nMilk: {stock["milk"]}ml\nCoffee: {stock["coffee"]}gm\n"
                  f"Money: ${stock["money"]}.")

        # To turn off the machine.
        elif order == "off":
            break

        # If the user entered a wrong beverage.
        elif order not in beverage_list:
            print("Wrong input!.")

        # Checking the available stock of ingredients.
        else:
            for item in stock:
                if item != "money":  # to eliminate the item (money) which is in stock keys but not in MENU keys.
                    if stock[item] < MENU[order]["ingredients"][item]:
                        print(f"Sorry there isn't enough {item}.")
                        making_beverage = False
            if making_beverage:
                collect_money(order)


# ---------------------------- STEP 2: MONEY COLLECTION ------------------------------- #


def collect_money(beverage):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total_in_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    change = round(total_in_money - float(MENU[beverage]["cost"]), 2)
    if change < 0:                              # which means the money entered is less than the cost of the beverage.
        print("Not enough money, money refunded.")
    else:
        make_beverage(beverage)
        print(f"Here is ${change} in change.")
        print(f"Here is your {beverage}☕, enjoy.")


# ---------------------------- STEP 3: MAKING THE BEVERAGE ------------------------------- #


def make_beverage(beverage):
    stock["water"] = int(stock["water"]) - int(MENU[beverage]["ingredients"]["water"])
    stock["milk"] = int(stock["milk"]) - int(MENU[beverage]["ingredients"]["milk"])
    stock["coffee"] = int(stock["coffee"]) - int(MENU[beverage]["ingredients"]["coffee"])
    stock["money"] = float(stock["money"]) + float(MENU[beverage]["cost"])


taking_order()
