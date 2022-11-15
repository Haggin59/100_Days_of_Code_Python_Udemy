import random
x = random.randint(1,100)
print("I have guessed a number between 1 and 100")
dif = int(input("Choose difficulty 1-Easy 2-Hard: "))

def Number_Guesser():
    #print(dif," ",x)
    if dif == 1:
        n = 10
    elif dif == 2:
        n = 5
        print(n)
    while n>0 :
        print(f"You have {n} guesses left")
        t = int(input("Enter Guess: ")) 
        n = n-1
        if t == x:
            print(f"You win with {n} guesses left")
            break  
        elif t > x:
            print("Too High")
        elif t < x:
            print("Too Low")    
        if n == 0:
            print(f"ooops!! The nuber was {x}")    
             
Number_Guesser()