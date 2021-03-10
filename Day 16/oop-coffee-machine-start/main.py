from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

userRequest = ''

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
isOn = True

while userRequest != "off":
    options = menu.get_items()
    userRequest = input(f"What would you like? {options}: ").lower()

    if userRequest == "off":
        isOn = False
    elif userRequest == "report":
        coffeeMaker.report()
    elif menu.find_drink(userRequest).name == userRequest:
        drink = menu.find_drink(userRequest)
        isEnoughIngredients = coffeeMaker.is_resource_sufficient(drink)
        isPaymentSucessful = moneyMachine.make_payment(drink.cost)
        if isEnoughIngredients and isPaymentSucessful:
            coffeeMaker.make_coffee(drink)