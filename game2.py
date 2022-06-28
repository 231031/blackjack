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
        if total_dealer > 21: 
            total_dealer = dealer.Check1_dealer() # Dealer card "A" total of the first time
            print("Total's Dealer = %d" % total_dealer)
        if total_player > 21:
            total_player = player.Check1_player() # Player card "A" total of the first time
            print("Total's Player = %d" % total_player)  
            
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
        print("Total's Player %d" % total_player)
        
        # if total's player more than 21 check "A" in ls_player
        while total_player > 21:
            total_player = player.Check_player()
            if total_player < 21: 
                print("Total's Player %d" % total_player)
        
        # check total
        # random Dealer
        if total_dealer <= 17:
            dealer.dealer_card()
            list_dealer = dealer.Show_ls_dealer()
            print(dealer.__str__())
            print(list_dealer) 
            total_dealer = dealer.Dealer_total()
            print("Total's Dealer = %d" % total_dealer)
            
            # if total's dealer more than 21 check A in ls_dealer
            while total_dealer > 21:
                total_dealer = dealer.Check_dealer()
                if total_dealer < 21:  
                    print("Total's Dealer = %d" % total_dealer)
        
        if total_dealer == 21 and total_player == 21:
            print("Draw")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()    
            
        elif total_dealer == 21:
            print("You're busted")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()
                
        # Player
        elif total_player == 21:
            print("You win")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()
            
            
        ######################################### STAND #########################################
    else:
        if total_player == 21 and total_dealer == 21:
            print("Draw")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()
        
        elif total_dealer == total_player and total_dealer < 21 and total_player < 21 and total_dealer > 17:
            print("Draw")
              
        elif total_player == 21:
            print("You win // Dealer loss")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()
                
        elif total_dealer <= 17:
            # Dealer
            dealer.dealer_card()
            list_dealer = dealer.Show_ls_dealer()
            print(dealer.__str__())
            print(list_dealer)
            total_dealer = dealer.Dealer_total()
            print("Total's Dealer = %d" % total_dealer)
            
            # if total's dealer more than 21 check A in ls_dealer
            while total_dealer > 21:
                total_dealer = dealer.Check_dealer()
                if total_dealer < 21:   
                    print("Total's Dealer = %d" % total_dealer)
            
        elif total_dealer > total_player and total_dealer > 17:
            print("You're busted")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()
                
        elif total_player > total_dealer and total_dealer > 17:
            print("You win//Dealer loss")
            new = (input("Do you want to play again? [Y/N]: ")).lower()
            if new == "y":
                continue
            else:
                exit()