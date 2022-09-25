# System controlling programme for Coffee Machines

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Starting details


def have_resource(drink):  # function 1
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            main_function()
            return


def process_coins():  # function 2
    print("Please insert coins.")
    total = int(input("How many quarters : ")) * 0.25
    total += int(input("How many dimes : ")) * 0.1
    total += int(input("How many nickels : ")) * 0.05
    total += int(input("How many pennies : ")) * 0.01

    return round(total, 3)


def manage_money(money_user, drink_cost, user_input):  # function 3
    if money_user > drink_cost:
        print(f"Here is ${round(money_user-drink_cost, 2)} in charge.")
        print(f"Here is your {user_input}. Enjoy it !!!")
    else:
        print("Sorry that's not enough money. Money refunded. ")
        main_function()


def update_resource(drink):  # function 4
    global profit
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]
    profit += drink['cost']


def process_user_input(input_user):  # function 5
    if input_user == "report":
        print(f"Water   :   {resources['water']}ml")
        print(f"Milk    :   {resources['milk']}ml")
        print(f"Coffee  :   {resources['coffee']}g")
        print(f"Profit  :   ${profit}")
        main_function()

    elif input_user in MENU:
        drink = MENU[input_user]
        have_resource(drink)  # finding whether resources available or not
        user_money = process_coins()  # finding how much money user enters
        manage_money(user_money, drink['cost'], input_user)  # finding whether user has entered enough money
        update_resource(drink)  # updating resources if a sell happened
        main_function()  # restart the programme


def main_function():
    print("\nWelcome To Coffee Machine !!!")
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input in MENU or user_input == 'report':
        process_user_input(user_input)
    else:
        exit()


main_function()
