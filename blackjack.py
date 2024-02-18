import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
krupier_cards = []
start = input("Welcome to the Blackjack game. Wrice 'y' if you want to continue")
if start == 'y':
    card1_player = random.choice(cards)
    card1_player = int(card1_player)
    card1_krupier = random.choice(cards)
    card1_krupier = int(card1_krupier)
    print(f"This is value of your card = {card1_player} \n This is value of krupier's card = {card1_krupier}")
    card2_player = random.choice(cards)
    card2_player = int(card2_player)
    card2_krupier = random.choice(cards)
    card1_krupier = int(card1_krupier)
    player_summary_value = card1_player + card2_player
    krupier_revealed_summary = card1_krupier
    krupier_unrevealed_summary = card1_krupier + card2_krupier
    print(f"This is value of your second card = {card2_player} \n This is summary value = {player_summary_value}. The revealed summary of krupier is {krupier_revealed_summary} ")
    while(player_summary_value < 21 or krupier_unrevealed_summary < 21 or player_summary_value == 21):
                continue3 = input("If you want to continue write 'y', if no - write 'n'. ")
                if continue3 == 'n':
                    if player_summary_value > 21:
                        print(f"YOU LOST! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")
                    elif krupier_unrevealed_summary > 21:
                        print(f"YOU WON! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")
                    else:
                        if krupier_unrevealed_summary < player_summary_value:
                            print(f"YOU WON! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")
                        elif krupier_unrevealed_summary == player_summary_value:
                            print(f"DRAW! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")
                        elif krupier_unrevealed_summary < player_summary_value:
                            print(f"YOU LOST! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")
                else:
                    if player_summary_value > 21 or krupier_unrevealed_summary > 21:
                        break
                    else:
                        card3_player = random.choice(cards) #3 and next
                        card3_player = int(card3_player)
                        card3_krupier = int(random.choice(cards))
                        player_summary_value += card3_player
                        krupier_unrevealed_summary += card3_krupier
                        print(f"This is value of your card = {card3_player} \n This is your summary value = {player_summary_value}. The revealed summary of krupier is {krupier_revealed_summary} ")
    print(player_summary_value, krupier_unrevealed_summary)
    if player_summary_value > 21:
                        print(f"YOU LOST! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")
    elif krupier_unrevealed_summary > 21:
                        print(f"YOU WON! \n krupier = {krupier_unrevealed_summary}, you = {player_summary_value}")     
                            





        
