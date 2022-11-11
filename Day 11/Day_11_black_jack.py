import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def draw_cards(cards):
    draw = random.choice(cards)
    return draw

def cond_ace(players_hand):
    if 11 in players_hand:
        n = players_hand.index(11)
        players_hand[n] = 1
        print(f"Player's hand: {players_hand} Total:",sum(players_hand))
    

players_hand = []
dealers_hand = []


def black_jack():
    flag = 0
    for i in range(2):                
        players_hand.append(draw_cards(cards))                #Initial Draw
        dealers_hand.append(draw_cards(cards))
    
    print(f"Player's hand: {players_hand} Total:",sum(players_hand))
    print(f"Dealer's hand: [X, {dealers_hand[0]}]")

    if sum(players_hand) == 22:
        cond_ace(players_hand)
    
    if sum(players_hand) < 21:
        draw = input("Do you wish to draw again (y/n)?")
    else:
        draw = 'n'    

    while(draw == 'y' and sum(players_hand)<21):              #Player's additional draw
        players_hand.append(draw_cards(cards))
        print(f"Player's hand: {players_hand} Total:",sum(players_hand))
        if sum(players_hand) == 21:
            break
        if sum(players_hand) > 21:
            cond_ace(players_hand)
            if sum(players_hand) > 21:
                flag = 1
                break
        draw = input("Do you wish to draw again (y/n)?")

        if flag != 1:
            while(sum(dealers_hand) < 17):                              #Dealer's additional draw <17'
                print('lflag',flag)
                dealers_hand.append(draw_cards(cards))

    print('gflag',flag)
    print(f"Player's hand: {players_hand} Total:",sum(players_hand))   #Final Result
    print(f"Dealer's hand: {dealers_hand} Total:",sum(dealers_hand))

    if(sum(dealers_hand) > sum(players_hand) and sum(dealers_hand) <= 21) or flag == 1:
        print("Dealer Wins")
    elif(sum(players_hand) > sum(dealers_hand) and sum(players_hand) <= 21 ):
        print("You win")  
    elif(sum(players_hand) == sum(dealers_hand) <=21 ):
        print("Draw")



black_jack()      

