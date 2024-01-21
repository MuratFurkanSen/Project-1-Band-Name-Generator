from data import MENU as menu

resources = {"water": 300, "coffee": 100, "milk": 200, "profit": 0}
while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "report":
        for res, val in resources.items():
            if res == "profit":
                print(f"{res}: ${val}")
            else:
                print(f"{res}: {val}ml")
        continue
    if choice not in menu.keys():
        print("Invalid Choice")
        continue

    chosenDrink = menu[choice]
    notEnoughRes = False
    for i in chosenDrink['ingredients'].keys():
        if resources[i] - chosenDrink['ingredients'][i] < 0:
            print(f"Sorry, there is not enough {i}")
            notEnoughRes = True
            break
    if notEnoughRes:
        continue

    print("Pls insert coins.")
    takenCoinsTotal = (int(input("How many quarters?: ")) * 0.25 +
                       int(input("How many dime?: "))     * 0.10 +
                       int(input("How many nickel?: "))   * 0.05 +
                       int(input("How many penny?: "))    * 0.01 )

    if takenCoinsTotal < chosenDrink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        continue

    for i in chosenDrink['ingredients']:
        resources[i] -= chosenDrink['ingredients'][i]

    print(f"Here is ${takenCoinsTotal - chosenDrink['cost']:.2f} in change.")
    print("Here is your latte ☕️. Enjoy!")
    resources["profit"] += chosenDrink["cost"]


