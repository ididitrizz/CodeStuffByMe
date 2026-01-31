#Blackjack Code
import random
Deck = ["A","A","A","A","2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
random.shuffle(Deck)
print(type(Deck))
#Deal
PHand=[]
DHand=[]
PHand.append(Deck.pop(0))
PHand.append(Deck.pop(0))
DHand.append(Deck.pop(0))
DHand.append(Deck.pop(0))
print("     Dealer is showing " + DHand[0])
print("     Your hand is " + str(PHand))
def Value(hand):
    card = 0
    value = 0
    A = 0
    while card < len(hand):
        if hand[card] == "A":
            value = value + 11
            A = A + 1
        elif hand[card] == "J" or hand[card] == "Q" or hand[card] == "K":
            value = value + 10
        else:
            value = value + int(hand[card])
        card = card + 1
    if value > 21 and A > 0:
        while value > 21 and A > 0:
            value = value - 10
            A = A - 1
    return value
    
Hit = 0
while not Hit == "2":
    Hit = input("     Hit or stand? Hit = 1 Stand = 2\n")
    if Hit == "1":
        PHand.append(Deck.pop(0))
        HandVal = Value(PHand)
        print("Your hand is now " + str(PHand) + ", worth " + str(HandVal))
        if HandVal > 21:
            print("Bust!")
            Hit = "2"
    else:
        if not Hit == 2:
            print("     Error: Type a 1 or a 2")
if Value(PHand) == 21 and len(PHand)== 2:
    print("You have a natural blackjack!")
    finalpval = 22
else:
    finalpval = Value(PHand)
#Dealer's turn
print("Dealer's hand is " + str(DHand))
while Value(DHand) < 16:
    print("Dealer hits")
    DHand.append(Deck.pop(0))
    print("Dealer now has " + str(DHand))
print("Dealer stands")
if Value(DHand) > 21:
    print("Dealer busts!")
if Value(DHand) == 21 and len(DHand) == 2:
    print("Dealer has natural blackjack.")
    finaldval = 22
else:
    finaldval = Value(DHand)
    
#Scoring
if finalpval > finaldval:
    print("You Win!")
else:
    print("You Lose.")

