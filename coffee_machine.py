MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
}

raport = resources
production = True

while(production == True):
    def money():
        print("Please insert money")
        quarters = 0.25*int(input("How many quarters: ?"))
        dimes = 0.10*int(input("How many dimes: "))
        nickles = 0.05*int(input("How many nickles: "))
        pennies = 0.01*int(input("How many pennies: "))
        deposit = quarters + dimes + nickles + pennies
        global cost
        if cost > deposit:
            print("Not enough money")
            production = False

        elif cost <= deposit:
            print(f"here is your change {deposit - cost}")
            print("Here is your coffee")
            resources_use()

    def resources_use():
        global water, milk, coffee
        resources["water"] = int(resources["water"]) - int(water)
        resources["milk"] = int(resources["milk"]) - int(milk)
        resources["coffee"] = int(resources["coffee"]) - int(coffee)
            
    def check_resources():
        global water, milk, coffee
        if water < resources["water"] and milk < resources["milk"] and coffee < resources["coffee"]:
            money()
        else:
            print("Not enough rescources!")
            production = False


    choice = input("What would you like? (espresso/latte/cappuccino)")

    if choice == 'espresso':  
        
        cost = MENU["espresso"]["cost"]
        water = MENU["espresso"]["ingredients"]["water"]
        milk = MENU["espresso"]["ingredients"]["milk"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        print(f"{cost}$")
        check_resources()
        

    elif choice == 'latte':
        cost = MENU["latte"]["cost"]
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        print(f"{cost}$")
        check_resources()

    elif choice == 'cappuccino':
        cost = MENU["cappuccino"]["cost"]
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"{cost}$")
        check_resources()
    elif choice == 'raport':
        print(raport)
