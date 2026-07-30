import random

suits = ["S", "H", "D", "C"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

def make_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    random.shuffle(deck)
    return deck

def card_value(card):
    return values[card[:-1]]

def hand_total(cards):
    total = 0
    for card in cards:
        total += card_value(card)
    for card in cards:
        if card[:-1] == "A" and total + 10 <= 21:
            total += 10
    return total

def show_hand(name, cards, hide_first=False):
    display = []
    for i, card in enumerate(cards):
        if i == 0 and hide_first:
            display.append("[??]")
        else:
            display.append("[" + card + "]")
    print(name + ":", " ".join(display))

def player_turn(deck, hand):
    while True:
        total = hand_total(hand)
        show_hand("Your hand", hand)
        print("  Total:", total)

        if total > 21:
            print("  Bust!")
            return total

        choice = input("Hit or stand? (H/S): ").strip().lower()
        if choice == "h" or choice == "hit":
            hand.append(deck.pop())
        elif choice == "s" or choice == "stand":
            return total
        else:
            print("  Enter H or S.")

def dealer_turn(deck, hand):
    show_hand("Dealer hand", hand)
    while True:
        total = hand_total(hand)
        if total > 21:
            print("  Dealer busts!")
            return total
        if total >= 17:
            print("  Dealer stands at", total)
            return total
        hand.append(deck.pop())
        show_hand("Dealer hand", hand)

def get_bet(money):
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
            if bet > 0 and bet <= money:
                return bet
            print("  Bet must be between 1 and " + str(money) + ".")
        except ValueError:
            print("  Enter a number.")

def main():
    print("Welcome to Blackjack!")
    money = 500

    while True:
        if money <= 0:
            print("\nYou ran out of money!")
            break

        print("\nBalance: $" + str(money))
        print("=" * 40)

        bet = get_bet(money)

        deck = make_deck()
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]

        show_hand("Dealer showing", dealer, hide_first=True)
        print()

        p_total = player_turn(deck, player)
        if p_total > 21:
            money -= bet
            print("\nYou lost $" + str(bet) + "!")
            continue

        print()
        d_total = dealer_turn(deck, dealer)

        print("\n" + "-" * 40)
        show_hand("Your hand", player)
        print("  Total:", p_total)
        show_hand("Dealer hand", dealer)
        print("  Total:", d_total)

        if d_total > 21 or p_total > d_total:
            money += bet
            print("\nYou won $" + str(bet) + "!")
        elif p_total == d_total:
            print("\nPush! Your bet is returned.")
        else:
            money -= bet
            print("\nYou lost $" + str(bet) + "!")

        while True:
            again = input("Play again? (Y/N): ").strip().lower()
            if again == "y" or again == "yes":
                break
            elif again == "n" or again == "no":
                print("\nFinal balance: $" + str(money))
                print("Thanks for playing!")
                return

    print("\nFinal balance: $0")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
