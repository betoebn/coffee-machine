from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    user_input = input(f"What would you like to drink?: {menu.get_items()}")
    drink = menu.find_drink(user_input)
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    if user_input == "off":
        print("Turning off")
        machine_on = False
        continue
    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

