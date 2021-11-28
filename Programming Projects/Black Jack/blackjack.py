import random
import sys
import time

#print slow

def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.04)

#Player + dealer Deck
        
def yourDeck1():
    yourDeck = 0
    yourAce = 0
    for i in range(2):
        r = random.randint(1,13)
        #r = random.randint(1,2)
        if r == 1:
            print_slow("You got Ace of ")
            suit()
            yourDeck += 11
            yourAce += 1
            if yourDeck > 21:
                yourDeck -= 10
                yourAce -= 1
        elif r == 10:
            print_slow("You got 10 of ")
            suit()
            yourDeck += 10
        elif r > 10:
            print_slow("You got ")
            faceCard()
            print_slow("of ")
            suit()
            yourDeck += 10
        elif r < 10:
            r = r
            print_slow("You got ")
            print(r, end=" ")
            print_slow("of ")
            suit()
            yourDeck += r
    print("")
    print_slow("Your Total Value: ")
    print(yourDeck)
    print("")
    yourDeck = {"yourDeck":yourDeck,"yourAce":yourAce}
    return yourDeck

def dealerDeck1():
    dealerDeck = 0
    dealerAce = 0
    r = random.randint(1,13)
    if r == 1:
        print_slow("Dealer got Ace of ")
        suit()
        dealerDeck += 11
        dealerAce += 1
    elif r == 10:
        print_slow("Dealer got 10")
        suit()
        print("")
        dealerDeck += 10
    elif r > 10:
        print_slow("Dealer got ")
        faceCard()
        print_slow("of ")
        suit()
        print("")
        dealerDeck += 10
    elif r < 10:
        r = r
        print_slow("Dealer got ")
        print(r, end=" ")
        print_slow("of ")
        suit()
        print("")
        dealerDeck += r
    dealerDeck = {"dealerDeck":dealerDeck,"dealerAce":dealerAce}
    return dealerDeck

#Your + Dealer moves

def yourChoice(dealerDeck, yourDeck):
    yourAce = yourDeck["yourAce"]
    yourDeck = yourDeck["yourDeck"]
    hos = int(input("Hit or Stay? 1 = Hit | 2 = Stay"))
    print("")
    while hos == 1:       
        r = random.randint(1,13)
        if r == 1:
            print_slow("You got Ace of ")
            suit()
            yourDeck += 11
            yourAce += 1
        elif r == 10:
            print_slow("You got 10 of ")
            suit()
            yourDeck += 10
        elif r > 10:
            print_slow("You got ")
            faceCard()
            print_slow("of ")
            suit()
            yourDeck += 10
        elif r < 10:
            print_slow("You got ")
            print(r, end=" ")
            print_slow("of ")
            suit()
            yourDeck += r
        if yourAce > 0:
            if yourDeck > 21:
                yourDeck -= 10
                yourAce -= 1
        if yourDeck > 21:
            print_slow("Your Total Value: ")
            print(yourDeck)
            print("")
            loser(dealerDeck, yourDeck)
        else:
            print_slow("Your Total Value: ")
            print(yourDeck)
            print("")
            hos = int(input("Hit or Stay? 1 = Hit | 2 = Stay"))
        if r == 2:
            break
    print_slow("Player stays \n")
    print("")
    return yourDeck

def dealerChoice(dealerDeck, yourDeck):
    dealerAce = dealerDeck["dealerAce"]
    dealerDeck = dealerDeck["dealerDeck"]
    if dealerDeck < yourDeck:
        r = random.randint(1,13)
        if r == 1:
            print_slow("Dealer got Ace of ")
            suit()
            dealerDeck += 11
            dealerAce += 1
            if dealerDeck > 21:
                dealerDeck -= 10
                dealerAce -= 1
        elif r == 10:
            print_slow("Dealer got 10 of ")
            suit()
            dealerDeck += 10
        elif r > 10:
            print_slow("Dealer got ")
            faceCard()
            print_slow("of ")
            suit()
            dealerDeck += 10
        elif r < 10:
            print_slow("Dealer got ")
            print(r, end=" ")
            print_slow("of ")
            suit()
            dealerDeck += r
    
        if dealerAce > 0:
            if dealerDeck > 21:
                dealerDeck -= 10
                dealerAce -= 1
        if dealerDeck > 21:
            print_slow("Dealer Total Value: ")
            print(dealerDeck)
            print("")
            loser(dealerDeck, yourDeck)
        else:
            print_slow("Dealer Total Value: ")
            print(dealerDeck)
            print("")
            dealerDeck = {"dealerDeck":dealerDeck,"dealerAce":dealerAce}
            dealerChoice(dealerDeck, yourDeck)
    else:
        print_slow("Dealer stays")
        print("")
        print(yourDeck,"vs",dealerDeck)
        winner(dealerDeck, yourDeck)

#loser and winner

        
def loser(dealerDeck, yourDeck):
    if dealerDeck == 21:
        print_slow("You Lose")
        print("")
        playAgain()
    elif yourDeck == 21:
        print_slow("You Win")
        print("")
        playAgain()
    elif yourDeck > 21:
        print_slow("You Lose")
        print("")
        playAgain()
    elif dealerDeck > 21:
        print_slow("You Win")
        print("")
        playAgain()


def winner(dealerDeck, yourDeck):
    if dealerDeck == 21:
        print_slow("You Lose")
        print("")
        playAgain()
    elif yourDeck == 21:
        print_slow("You Win")
        print("")
        playAgain()
    elif dealerDeck > 21:
        print_slow("You Win")
        print("")
        playAgain()
    elif yourDeck > 21:
        print_slow("You Lose")
        print("")
    elif dealerDeck < yourDeck:
        print_slow("You Win")
        print("")
        playAgain()
    elif dealerDeck >= yourDeck:
        print_slow("You Lose")
        print("")
        playAgain()

#Suit and Face Cards

def suit():
    suit = random.randint(1,4)
    if suit == 1:
        print_slow("Spades \n")
    elif suit == 2:
        print_slow("Clubs \n")
    elif suit == 3:
        print_slow("Hearts \n")
    elif suit == 4:
        print_slow("Diamonds \n")
    return suit

def faceCard():
    faceCard = random.randint(1,3)
    if faceCard == 1:
        print_slow("Jack ")
    elif faceCard == 2:
        print_slow("Queen ")
    elif faceCard == 3:
        print_slow("King ")
    
#Black Jack and Play Again

def blackJack():
    yourDeck = yourDeck1()
    dealerDeck = dealerDeck1()
    yourDeck2 = yourChoice(dealerDeck, yourDeck)
    dealerChoice(dealerDeck, yourDeck2)
    
def playAgain():
    print("")
    h = int(input("Play Again? 1 = Yes | 2 = No"))
    print("")
    if h == 1:
        blackJack()
    elif h == 2:
        sys.exit()

#program
        
blackJack()
