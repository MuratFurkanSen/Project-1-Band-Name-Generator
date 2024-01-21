from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
machine = CoffeeMaker()
coin_handler = MoneyMachine()
coffees = Menu()
while is_on:
    choice = input(f"What would you like? ({coffees.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine.report()
        coin_handler.report()
    else:
        drink = coffees.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            if coin_handler.make_payment(drink.cost):
                machine.make_coffee(drink)





