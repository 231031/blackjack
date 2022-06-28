# from blackjack_start import Start
from tracemalloc import stop
from player import Player
from dealer import Dealer
print("Welcome to Blackjack Game")
i = 1
j = 1
while True:
    ########################################## start game just first times #########################################
    if i == 1: 
        player = Player() # create object Player
        dealer = Dealer()
        total_player = player.Total_first_p() # total of the first time
        total_dealer = dealer.Total_first_d()
        list_player = player.Show_ls_player() # list of card
        list_dealer = dealer.Show_ls_dealer()
        
        # check for use special card "A" at first game
        if total_dealer > 21 or total_player > 21:
            # Player card "A"
            for card_player in list_player:
                if card_player == "A":
                    total_player = total_player -10
                elif card_player == list_player[len(list_player) - 1]:
                    print("You're busted")
                    exit()
            # Dealer card "A"
            for card_dealer in list_dealer:
                if card_dealer == "A":
                    total_dealer = total_dealer - 10
                elif card_dealer == list_dealer[len(list_dealer) - 1]:
                    print("You win")
                    exit()
        
        print("Total's Player = %d" % total_player)
        print("Total's Dealer = %d" % total_dealer)
        i = 2
     
    ######################################### Next round #########################################   
    choice = input("Do you want to Hit or Stand [H/S]: ").lower()
    
    ######################################### HIT #########################################
    if choice == "h":        
        # random Player
        player.player_card()
        list_player = player.Show_ls_player()
        print(player.__str__())
        print(list_player)
        total_player = player.Player_total()
        
        # if total's player more than 21 check "A" in ls_player
        if total_player > 21:
            # Player card "A"
            for card_player in list_player:
                if card_player == "A" and i == 2:
                    total_player = total_player - 10
                    i = 3
                elif card_player == list_player[len(list_player) - 1]:
                    print("You're busted")
                    exit()
        print("Total's Player %d" % total_player)
        
        # check total
        # random Dealer
        if total_dealer <= 17:
            dealer.dealer_card()
            list_dealer = dealer.Show_ls_dealer()
            print(dealer.__str__())
            print(list_dealer) 
            total_dealer = dealer.Dealer_total()
            
            # if total's dealer more than 21 check A in ls_dealer
            if total_dealer > 21:
                for card_dealer in list_dealer:
                    if card_dealer == "A" and j == 1:
                        total_dealer = total_dealer - 10
                        j = 2
                    elif card_dealer == list_dealer[len(list_dealer) - 1]:
                        print("You win//Dealer loss")
                        exit()
            print("Total's Dealer = %d" % total_dealer)
        
        if total_dealer == 21 and total_player == 21:
            print("Draw")
            exit()    
            
        elif total_dealer == 21:
            print("You're busted")
            exit()
        # Player
        elif total_player == 21:
            print("You win")
            exit()
        ######################################### STAND #########################################
    else:
        if total_player == 21 and total_dealer == 21:
            print("Draw")
            exit()
        elif total_player == 21:
            print("You win // Dealer loss")
            exit()
        elif total_dealer <= 17:
            # Dealer
            dealer.dealer_card()
            list_dealer = dealer.Show_ls_dealer()
            print(dealer.__str__())
            print(list_dealer)
            total_dealer = dealer.Dealer_total()
            
            # if total's dealer more than 21 check A in ls_dealer
            if total_dealer > 21:
                for card_dealer in list_dealer:
                    if card_dealer == "A" and (j == 1 or j == 2):
                        total_dealer = total_dealer - 10
                        j = 3
                    elif card_dealer == list_dealer[len(list_dealer) - 1]:
                        print("You win//Dealer loss")
                        exit()
            print("Total's Dealer = %d" % total_dealer)
        elif total_dealer > total_player and total_dealer > 17:
            print("You're busted")
            exit()
        elif total_player > total_dealer and total_dealer > 17:
            print("You win//Dealer loss")
            exit()