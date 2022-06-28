import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

class Start:
    # start game random 2 card
    def __init__(self):
        self.card1 = random.choice(deck)
        deck.remove(self.card1)
        self.card2 = random.choice(deck)
        deck.remove(self.card2)
    
    # random when Hit   
    def card(self):
        self.card = random.choice(deck)
        deck.remove(self.card)
    
    # display when game start  
    def __str__(self):
        if self.card1 == 11:self.card1 = "J"
        if self.card1 == 12:self.card1 = "Q"
        if self.card1 == 13:self.card1 = "K"
        if self.card1 == 14:self.card1 = "A"
        if self.card2 == 11:self.card2 = "J"
        if self.card2 == 12:self.card2 = "Q"
        if self.card2 == 13:self.card2 = "K"
        if self.card2 == 14:self.card2 = "A"
        return str(self.card1) +  "\n" + str(self.card2) + "\n" + str(self.card)
    