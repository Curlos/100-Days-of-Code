MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
userRequest = ''

while userRequest != "off":
    userRequest = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if userRequest == "report":
        for resource, value in resources.items():
            if resource == 'water' or resource == 'milk':
                print(f"{resource}: {value}ml")
            elif resource == 'coffee':
                print(f"{resource}: {value}g")
            elif resource == 'money':
                print(f"{resource}: ${value}")
    elif userRequest in MENU:
        ingredients = MENU[userRequest]["ingredients"]
        sufficient = True

        for ingredient, value in ingredients.items():
            if resources[ingredient] < value:
                print(f"Sorry there is not enough {ingredient}")
                sufficient = False
                break

        if sufficient:
            print('Please insert coins.')
            try:
                quarters = int(input('How many quarters? '))
                dimes = int(input('How many dimes? '))
                nickels = int(input('How many nickels? '))
                pennies = int(input('How many pennies? '))
            except ValueError:
                print('Invalid number entered.')

            totalMoney = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

            if totalMoney >= MENU[userRequest]["cost"]:
                resources["money"] += MENU[userRequest]["cost"]
                totalMoney -= MENU[userRequest]["cost"]

                for ingredient, value in ingredients.items():
                    resources[ingredient] -= value

                print(f"Here is ${round(totalMoney, 2)} in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")



# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.


