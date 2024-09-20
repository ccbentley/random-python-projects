import random

def deal_cards(cards_arr, amount: int, display_cards_arr) -> None:
    for card in range(amount):
        random_card_value: int = random.randrange(1,13)
        if random_card_value == 1:
            display_cards_arr.append("[A]")
            cards_arr.append(1)
        elif random_card_value == 11:
            display_cards_arr.append("[J]")
            cards_arr.append(10)
        elif random_card_value == 12:
            display_cards_arr.append("[Q]")
            cards_arr.append(10)
        elif random_card_value == 13:
            display_cards_arr.append("[K]")
            cards_arr.append(10)
        else:
            display_cards_arr.append("[" + str(random_card_value) + "]")
            cards_arr.append(random_card_value)


def add_card(cards_arr, display_cards_arr) -> None:
    random_card_value: int = random.randrange(1, 13)
    if random_card_value == 1:
        display_cards_arr.append("[A]")
        cards_arr.append(1)
    elif random_card_value == 11:
        display_cards_arr.append("[J]")
        cards_arr.append(10)
    elif random_card_value == 12:
        display_cards_arr.append("[Q]")
        cards_arr.append(10)
    elif random_card_value == 13:
        display_cards_arr.append("[K]")
        cards_arr.append(10)
    else:
        display_cards_arr.append("[" + str(random_card_value) + "]")
        cards_arr.append(random_card_value)
    
def calc_total_cards(cards_arr) -> int:
    total_cards: int = 0
    for card in cards_arr:
        total_cards += card
    return total_cards

playing: bool = True
money: int = 500

while playing:
    print("------------------------------------")
    print("Current Balance:", money)
    bet_money: int = -1
    while bet_money > money or bet_money < 0:
        bet_money: int = int(input("How Much Money Would You Like To Bet?: "))
    player_cards = []
    dealer_cards = []
    display_player_cards = []
    display_dealer_cards = []
    deal_cards(player_cards, 1, display_player_cards)
    total_player_cards: int = calc_total_cards(player_cards)
    print("Your Cards:", display_player_cards)
    stand: bool = False
    while not stand:
        print("------------------------------------")
        choice = str(input("Would you like to hit or stand? (H/S): "))
        if choice == "H" or choice == "h":
            add_card(player_cards, display_player_cards)
            total_player_cards = calc_total_cards(player_cards)
            print("Your Cards:", display_player_cards)
            if total_player_cards == 21:
                stand = True
            elif total_player_cards > 21:
                stand = True
            elif len(player_cards) > 5:
                stand = True
        elif choice == "S" or choice == "s":
            stand = True
    print("------------------------------------")

    deal_cards(dealer_cards, 3, display_dealer_cards)

    total_player_cards = calc_total_cards(player_cards)
    total_dealer_cards: int = calc_total_cards(dealer_cards)

    if total_dealer_cards < 19:
        add_card(dealer_cards, display_dealer_cards)
    
    total_dealer_cards = calc_total_cards(dealer_cards)

    for card in player_cards:
        if card == 1:
            valid: bool = False
            while not valid:
                ace_choice: str = str(input("What would you like your ace to be worth (A: 1) (B: 11): "))
                if ace_choice == "A" or ace_choice == "a":
                    valid = True
                elif ace_choice == "B" or ace_choice == "b":
                    valid = True
                    total_player_cards += 10

    for card in dealer_cards:
        if card == 1:
            if total_dealer_cards + 10 <= 21:
                total_dealer_cards += 10
            else:
                pass

    won: bool = False

    print("------------------------------------")
    print("Your Cards:", display_player_cards, total_player_cards)
    print("Dealer Cards:", display_dealer_cards, total_dealer_cards)
    print("------------------------------------")

    if total_player_cards <= 21 and total_player_cards > total_dealer_cards:
        won = True
    elif total_dealer_cards <= 21:
        won = False
    else:
        won = True

    if won:
        print("You Beat The Dealer!")
        money -= bet_money
        print("Money:", money)
    else:
        print("You Lost!")
        money -= 0
        print("Money:", money)
    
    print("------------------------------------")
    play_again_choice: str = input("Would you like to play again? (Y/N): ")
    if play_again_choice == "Y" or play_again_choice == "y":
        playing = True
    elif play_again_choice == "N" or play_again_choice == "n":
        playing = False
    print("------------------------------------\n")