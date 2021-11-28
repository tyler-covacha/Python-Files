import random
import string
import sys
import time


''' print slow '''      # for ui purposes
def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.04)
        
def print_space_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.1)


class black_jack:
    
    def __init__(self):
        self.player_ace_counter = 0
        self.dealer_ace_counter = 0
        self.player_hand_value = 0
        self.dealer_hand_value = 0
        self.deck_of_cards = {'King of Diamonds':10,
                              'King of Hearts':10,
                              'King of Clubs':10,
                              'King of Spades':10,
                              'Queen of Diamonds':10,
                              'Queen of Hearts':10,
                              'Queen of Clubs':10,
                              'Queen of Spades':10,
                              'Jack of Diamonds':10,
                              'Jack of Hearts':10,
                              'Jack of Clubs':10,
                              'Jack of Spades':10,
                              '10 of Diamonds':10,
                              '10 of Hearts':10,
                              '10 of Clubs':10,
                              '10 of Spades':10,
                              '9 of Diamonds':9,
                              '9 of Hearts':9,
                              '9 of Clubs':9,
                              '9 of Spades':9,
                              '8 of Diamonds':8,
                              '8 of Hearts':8,
                              '8 of Clubs':8,
                              '8 of Spades':8,
                              '7 of Diamonds':7,
                              '7 of Hearts':7,
                              '7 of Clubs':7,
                              '7 of Spades':7,
                              '6 of Diamonds':6,
                              '6 of Hearts':6,
                              '6 of Clubs':6,
                              '6 of Spades':6,
                              '5 of Diamonds':5,
                              '5 of Hearts':5,
                              '5 of Clubs':5,
                              '5 of Spades':5,
                              '4 of Diamonds':4,
                              '4 of Hearts':4,
                              '4 of Clubs':4,
                              '4 of Spades':4,
                              '3 of Diamonds':3,
                              '3 of Hearts':3,
                              '3 of Clubs':3,
                              '3 of Spades':3,
                              '2 of Diamonds':2,
                              '2 of Hearts':2,
                              '2 of Clubs':2,
                              '2 of Spades':2,
                              'Ace of Diamonds':11,
                              'Ace of Hearts':11,
                              'Ace of Clubs':11,
                              'Ace of Spades':11}
        

    ''' picks random card from deck '''
    def pick_random_card(self, hand, ace_counter):

        # pick random card
        card, value = random.choice(list(self.deck_of_cards.items()))
        print(card)
        
        # card value added to total value of player/dealer
        hand += value
        
        # if card is an ace, ace counter += 1
        if hand == 11:
            ace_counter += 1
                
        # if total hand over 21
            while hand > 21:
                
            # check if there is an ace (while ace counter > 0)
                while ace_counter > 0:
                    
                # ace will be valued at 1 instead of 11, total changes
                    hand -= 10
                    ace_counter -= 1
                            
        # remove card from dictionary
        del self.deck_of_cards[card]

        return hand, ace_counter


    ''' player's first two cards '''
    def player_first_two_cards(self):

        # for loop for player's first two cards
        for i in range(2):
            print_slow('You got: ')
            print()

            # picks random card from deck
            self.pick_random_card(self.player_hand_value,self.player_ace_counter)
            
        print_slow('Your total value: ')
        print(self.player_hand_value)
        print()
            

    ''' dealer's first two cards '''
    def dealer_first_two_cards(self):
        print_slow('Dealer got: ')
        print()
        
        # picks random card from deck
        pick_random_card(self.dealer_hand_value,self.dealer_ace_counter)
        

    ''' player decided to hit or stay '''
    def player_choice(self):
        'hi'

        # player decides to hit or stay
        # while player mistypes, error and retype
        # while player hits
            # picks random card from deck   pick_random_card(self.player_hand_value,self.player_ace_counter):
            # if player's deck > 21
                # player loses
            # player decides to hit or stay
            # if player decides to stay
                #print_slow("Player stays \n")
                #break


    ''' dealer decides to hit or stay '''   
    def dealer_choice(self):
        'hi'

        # dealer decides to hit or stay     while loop
            # picks random card from deck
            # if dealer's deck > 21
                # dealer loses
            # dealer decides to hit or stay
            # if dealer decides to stay
                #print_slow("Dealer stays \n")
                #break


    ''' determine who wins '''
    def player_loses():
        'hi'

    def dealer_loses():
        'hi'

    def player_vs_dealer_totals(self):
        'hi'


    ''' player decides to play again or not'''
    def play_again():
        'hi'
        

def play_black_jack():
    game = black_jack()
    game.player_first_two_cards()
    game.dealer_first_two_cards()
    # player's choice to either hit or stay
    # dealer's choice to either hit or stay
    # determines who wins


if __name__ == '__main__':
    play_black_jack()


