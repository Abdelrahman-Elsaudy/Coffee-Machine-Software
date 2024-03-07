# Coffee Machine

---

- This program represents the software of a coffee machine that can make 3 types of drinks: espresso, cappuccino and latte.
- After you choose your beverage it checks to see if it has enough stock of ingredients to make it.
- If so, it asks you to insert money, gives you the change and serves you the drink ☕.
- You can order more drinks if it has enough resources.
- The drinks and their ingredients and cost are written inside a variable called `MENU` as JSON format.

---

## Applied Skills:
- Functions with inputs and outputs.
- Logical if statements.
- While loops.
- List comprehension.
- JSON format manipulation.

---

## Explaining The Code in Three Steps:

---

**1. Taking The Order**

- I used a while loop in that function so the machine keeps taking orders.
```
def taking_order():
    machine_on = True
    while machine_on:
        making_beverage = True
        order = input("What would you like? (espresso, latte, cappuccino) or type 'report': ").lower()
```
- Alongside with taking beverage orders, the machine can give you 3 other responses:
    - Print the available stock at any stage when the user types "report".
    - Turn off the machine when the user types "off"
    - Print "Wrong Input" when the user types an unavailable beverage.
- To take the order, it first checks whether there are enough stock of resources to make the requested beverage,
if so, it moves to the next step which is: `collect_money(order)`.
```
    else:
        for item in stock:
            if item != "money":  # to eliminate the item (money) which is in stock keys but not in MENU keys.
                if stock[item] < MENU[order]["ingredients"][item]:
                    print(f"Sorry there isn't enough {item}.")
                    making_beverage = False
        if making_beverage:
            collect_money(order)
```

**2. Collecting Money**

- A function that starts with asking the user to enter quarters, dimes, nickles and pennies calculate the total money entered.
```
def collect_money(beverage):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total_in_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
```

- Then it checks whether the total money entered is enough to make the requested beverage or not, if so it calls the 
`making_beverage(beverage)` function and gives the user his change.
```    
    change = round(total_in_money - float(MENU[beverage]["cost"]), 2)
    if change < 0: 
        print("Not enough money, money refunded.")
    else:
        make_beverage(beverage)
        print(f"Here is ${change} in change.")
        print(f"Here is your {beverage}☕, enjoy.")
```

**3. Making The Beverage**

- A function that subtracts the beverage ingredients from the machine stock ingredients and adds the beverage cost to the 
stock money.
```    
def make_beverage(beverage):
    stock["water"] = int(stock["water"]) - int(MENU[beverage]["ingredients"]["water"])
    stock["milk"] = int(stock["milk"]) - int(MENU[beverage]["ingredients"]["milk"])
    stock["coffee"] = int(stock["coffee"]) - int(MENU[beverage]["ingredients"]["coffee"])
    stock["money"] = float(stock["money"]) + float(MENU[beverage]["cost"])
```

---

## To be Improved:
- Using Object-Oriented Programming, I did this already in a separate repository.
- Making a simple GUI with Tkinter.
---

_Credits to: 100-Days of Code Course on Udemy._