from blackjack_start import Start
from ast import Global
#################### for player ####################

class Player(Start):
    def __init__(self):
        self.ls_player = []
        print("Player's hand")
        super().__init__()
        if self.card1 == 11:self.card1 = "J"
        if self.card1 == 12:self.card1 = "Q"
        if self.card1 == 13:self.card1 = "K"
        if self.card1 == 14:self.card1 = "A"
        if self.card2 == 11:self.card2 = "J"
        if self.card2 == 12:self.card2 = "Q"
        if self.card2 == 13:self.card2 = "K"
        if self.card2 == 14:self.card2 = "A"
        self.ls_player.clear()
        self.ls_player.append(self.card1)
        self.ls_player.append(self.card2)
        print(super().__str__())
    
    # Method calculate total of player at the first game    
    def Total_first_p(self):
        self.total_first_p = 0
        for score in self.ls_player:
            if score == "Q" or score == "J" or score == "K":
                self.total_first_p += 10
            elif score == "A":
                self.total_first_p += 11
            else:
                self.total_first_p += int(score)
        return self.total_first_p
    
    # Check for use special card "A"
    def Check1_player(self):
        for card_player in self.ls_player:
            if card_player == "A":
                self.total_first_p = self.total_first_p - 10
                break
            elif card_player == self.ls_player[len(self.ls_player) - 1]:
                print("You're busted")
                exit()
        return self.total_first_p
    
    # Method show card of player
    def __str__(self, out_card = "Player's hand"):
        self.out_card = out_card
        self.out_card += "\n"
        for show in self.ls_player:
            self.out_card += str(show)
            self.out_card += '\n'
        return self.out_card
    
    def Show_ls_player(self):
        return self.ls_player
    
    # Method random player card
    def player_card(self):
        super().card()
        if self.card == 11:self.card = "J"
        if self.card == 12:self.card = "Q"
        if self.card == 13:self.card = "K"
        if self.card == 14:self.card = "A"
        self.ls_player.append(self.card)
    
    # Method calculate score of Player
    def Player_total(self):
        self.total_p = 0
        for score in self.ls_player:
            if score == "Q" or score == "J" or score == "K":
                self.total_p += 10
            elif score == "A":
                self.total_p += 11
            else:
                self.total_p += int(score)
        return self.total_p
    
    def Check_player(self):
        for card_player in self.ls_player:
            if card_player == "A":
                self.total_p = self.total_p - 10
                break
            
            # continue have to stay in loop 
            # remove elif to the game so that they will be in while loop to use continue
            # fix ask for play again before exit program
            elif card_player == self.ls_player[len(self.ls_player) - 1]:
                print("You're busted")
                exit()
        return self.total_p
        