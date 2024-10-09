import time

import hand

player_hand = hand.Hand()
house_hand = hand.Hand()

print("Blackjack! Enter any key to continue.")
input("")


def deal():
    print("------------\n Dealing...\n------------\n\n\n")

    time.sleep(1)

    player_hand.start_hand("Your")
    house_hand.start_hand("House", True)

    play()

# replay
def go_again():
    # ask to go again
    inp = input("Go again?")

    # replace spaces with nothing and change to lowercase
    inp.replace(" ", "").lower()
    if inp == "y" or inp == "":
        # start again if so
            deal()

def play():

    # PLAYERS TURN
    cont = True

    while cont:
        if player_hand.hand_sum > 21:
                print(f"Bust!\n-------------\n")
                break
        elif player_hand.hand_sum == 21:
                print(f"Blackjack!\n-------------\n")
                break

        match input("\nHit or stand?\n"):
            case "h":
                player_hand.deal_card(False)
                print(f"New hand: {player_hand.cards_string}, Sum of: {player_hand.hand_sum}")
                time.sleep(0.5)


            case "s":
                print(f"Standing with: {player_hand.cards_string}, Sum of: {player_hand.hand_sum}\n")
                time.sleep(2)
                cont = False

    # STOOD, DEALERS TURN

    print(f"House's hand: {house_hand.cards_string}, Sum of: {house_hand.hand_sum}\n")
    while house_hand.hand_sum < 17: # draw if under 17 card sum
        # if the house's hand is greater than player's hand
        time.sleep(2)

        # if house's hand is greater than 21 (busted)
        if house_hand.hand_sum > 21:
            print("HOUSE BUSTED")

            # draw if both bust
            if player_hand.hand_sum > 21:
                print("Draw!")
                go_again()
            else:
                # player wins if house hand is bust
                print("You win!")
                go_again()
        # draw again
        else:
            house_hand.deal_card()
            print(f"House new hand: {house_hand.cards_string}, Sum of: {house_hand.hand_sum}\n")


    # go again if player's hand is greater than house's hand
    if house_hand.hand_sum < player_hand.hand_sum < 22:
        print("You win!")
        go_again()

    # handle drawing
    elif player_hand.hand_sum == house_hand.hand_sum:

        # if both blackjack, whoever has the fewer cards win
        if player_hand.hand_sum == 21:
            if len(player_hand.cards) < house_hand.cards:
                print("Player Wins! Less cards in 21")
            else:
                print("House Wins! Less cards in 21")
        else:
            print("Draw!")
            go_again()
    else:
        if house_hand.hand_sum > 21:
            print("House busts! You win!")
            go_again()
        else:
            print("House wins!")
            go_again()



# kickstart the game
deal()