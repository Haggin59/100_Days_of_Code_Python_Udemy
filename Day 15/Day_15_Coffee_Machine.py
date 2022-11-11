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
    "Money" : 0
}


def CheckResource(choice):
    flag = 1
    for ke in MENU[choice]["ingredients"].keys():
        #print(MENU[choice]["ingredients"][ke]," --- ",resources[ke])
        if resources[ke] < MENU[choice]["ingredients"][ke]:
            flag = 0
            ind = ke
            break
    if flag == 0:
        return False,ke
    else:
        return True,ke

def ProcessCoins():
    q = int(input("How many Quarters: "))
    d = int(input("How many Dimes: "))
    n = int(input("How many Nickels: "))
    p = int(input("How many Pennies: "))

    total = q*0.25 + d*0.10 + n*0.05 + p*0.01
    #print("$",total)
    return total

def OrderProcessing(cash_in):
    if cash_in >= MENU[choice]["cost"]:
        resources["Money"] += MENU[choice]["cost"]
        if cash_in > MENU[choice]["cost"]:
            print("Here's $",round(cash_in - MENU[choice]["cost"],2)," in change")
            
        MakeCoffee()

    else:
        print("Sorry that's not enough money, Money refunded")

def MakeCoffee():
    for ke in MENU[choice]["ingredients"].keys():
        resources[ke] = resources[ke] - MENU[choice]["ingredients"][ke]
    print(f"Enjoy Your {choice}")


while(True):
    choice = input("What would you like? (espresso/latte/cappuccino): ")
     
    if choice == "off":
         break

    elif choice == "report":
        for i,j in resources.items():
            print(i," : ",j)

    else:
        if not CheckResource(choice)[0] :
            print(f"Not enough {CheckResource(choice)[1]} in stock")
        else:
            print("Enter Coins: ")   
            Money_in = round(ProcessCoins(),2)
            print("$",Money_in)
            OrderProcessing(Money_in)
            
    

    

