from menu import MENU

stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

beverage_list = [beverage for beverage in MENU]


def take_order():
    order_coffee = True               # this will be used later when we want to exit, we switch it to False.
    while order_coffee:
        beverage = input("What would you like? (espresso, latte, cappuccino) or type 'report': ").lower()
        if beverage == "report":      # a feature in the machine to print the available stock at any moment.
            print(f"Water: {stock["water"]}ml\nMilk: {stock["milk"]}ml\nCoffee: {stock["coffee"]}gm\n"
                  f"Money: ${stock["money"]}.")
        elif beverage == "off":      # a feature to turn off the machine.
            order_coffee = False
        elif beverage not in beverage_list:
            print("Wrong input!.")
            take_order()
        else:
            for item in stock:
                if item != "money":   # to eliminate the item (money) which is in stock keys but not in MENU keys.
                    if stock[item] < MENU[beverage]["ingredients"][item]:
                        print(f"Sorry there isn't enough {item}.")
                        order_coffee = False
            if order_coffee == True:
                collect_money(beverage)


def collect_money(beverage):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total_in_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    change = total_in_money - float(MENU[beverage]["cost"])
    rounded_change = round(change, 2)
    if change < 0:                              # which means the money entered is less than the cost of the beverage.
        print("Not enough money, money refunded.")
    else:
        make_beverage(beverage)
        print(f"Here is ${rounded_change} in change.")
        print(f"Here is your {beverage}☕, enjoy.")


def make_beverage(beverage):
    stock["water"] = int(stock["water"]) - int(MENU[beverage]["ingredients"]["water"])
    stock["milk"] = int(stock["milk"]) - int(MENU[beverage]["ingredients"]["milk"])
    stock["coffee"] = int(stock["coffee"]) - int(MENU[beverage]["ingredients"]["coffee"])
    stock["money"] = float(stock["money"]) + float(MENU[beverage]["cost"])


take_order()
