from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


order_res = CoffeeMaker()
order_mon = MoneyMachine()
choice = Menu()           #object of MENU


while 1:
    order = input(choice.get_items())        #prints menu, recieves users choice
    if order == 'off':
        break

    elif order == 'report':
        order_res.report()
        order_mon.report()
    
    else:

        choice_accepted = choice.find_drink(order) #returns a MenuItem obj

        if order_res.is_resource_sufficient(choice_accepted):          #checking for resources

            if order_mon.make_payment(choice_accepted.cost):           #collecting coins, refund
                order_res.make_coffee(choice_accepted)                 #make_coffee,deduct resources & add profit

