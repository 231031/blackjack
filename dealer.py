from blackjack_start import Start
#################### for dealer ####################
class Dealer(Start):
    def __init__(self):
        self.ls_dealer = []
        print("Dealer's hand")
        super().__init__()
        if self.card1 == 11:self.card1 = "J"
        if self.card1 == 12:self.card1 = "Q"
        if self.card1 == 13:self.card1 = "K"
        if self.card1 == 14:self.card1 = "A"
        if self.card2 == 11:self.card2 = "J"
        if self.card2 == 12:self.card2 = "Q"
        if self.card2 == 13:self.card2 = "K"
        if self.card2 == 14:self.card2 = "A"
        self.ls_dealer.clear()
        self.ls_dealer.append(self.card1)
        self.ls_dealer.append(self.card2)
        print(str(self.card1) + "\n" + str(self.card2))
        
    #def __str__(self):
    #    return str(self.card1) +  "\n" + str(self.card2) + "\n" + str(self.card)
    
    def Total_first_d(self):
        self.total_first_d = 0
        for score in self.ls_dealer:
            if score == "Q" or score == "J" or score == "K":
                self.total_first_d += 10
            elif score == "A":
                self.total_first_d += 11
            else:
                self.total_first_d += int(score)
        return self.total_first_d
    
    def Check1_dealer(self):
        for card_dealer in self.ls_dealer:
            if card_dealer == "A":
                self.total_first_d = self.total_first_d - 10
                break
            elif card_dealer == self.ls_dealer[len(self.ls_dealer) - 1]:
                print("You win")
                exit()
        return self.total_first_d
    
    
    def dealer_card(self):
        super().card()
        if self.card == 11:self.card = "J"
        if self.card == 12:self.card = "Q"
        if self.card == 13:self.card = "K"
        if self.card == 14:self.card = "A"
        self.ls_dealer.append(self.card)
        
    def __str__(self, out_card_d = "Dealer's hand"):
        self.out_card_d = out_card_d
        self.out_card_d += "\n"
        for show in self.ls_dealer:
            self.out_card_d += str(show)
            self.out_card_d += '\n'
        return self.out_card_d
    
    def Show_ls_dealer(self):
        return self.ls_dealer
 
    def Dealer_total(self):
        self.total_d = 0
        for score_d in self.ls_dealer:
            if score_d == "Q" or score_d == "J" or score_d == "K":
                self.total_d += 10
            elif score_d == "A":
                self.total_d += 11
            else:
                self.total_d += int(score_d)
        return self.total_d
    
    def Check_dealer(self):
        for card_dealer in self.ls_dealer:
            if card_dealer == "A":
                self.total_d = self.total_d - 10
                break
            elif card_dealer == self.ls_dealer[len(self.ls_dealer) - 1]:
                print("You win//Dealer loss")
                new = (input("Do you want to play again? [Y/N]: ")).lower()
                if new == "y":
                    continue
                else:
                    exit()
        return self.total_d