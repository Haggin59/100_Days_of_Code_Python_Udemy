# from turtle import Turtle,Screen

# t1 = Turtle()  #object of Turtle class
# window = Screen()        #object of Screen class

# t1.shape('square')          #methods of t1...
# t1.color('blue')
# t1.forward(100)

# window.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name",['Thor','Stark','Cap','Nat','Clint','Hulk'])
table.add_column("Power",['lightning','Suit','Super-Soldier','Nothin','Bulls-eye','Smash'])
table.align = 'l'

print(table)

