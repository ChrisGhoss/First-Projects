def get_cards():
    print("What 2 cards did you get? ")
    print("Input should be an integer from 1 to 10")
    cards = []
    while True:
        for i in range(2):
            while True:
                try:
                    card = int(input(f"Card #{i+1}: "))
                    if card > 0 and card <= 10:
                        cards.append(card)
                        break
                    else:
                        print("Your integer should be from 1 to 10!")
                except:
                    print("Please make sure your integer is from 1 to 10")
        break
    return cards

def get_dealer_card():
    print("Input should be an integer from 2 to 11")
    print(("What card did the dealer get?"))
    while True:
        try:
            card = int(input("Dealer's card: "))
            if card > 0 and card <= 10:
                return card
            else:
                print("Your integer should be from 1 to 10!")
        except:
            print("Please make sure your integer is from 1 to 10")

def is_blackjack(cards):
    for i in range(2):
        if cards[i] == 1:
            if i == 0:
                if 11 + cards[1] == 21:
                    print("BLACKJACK! No action needed")
                    return True
            elif i == 1:
                if 11 + cards[0] == 21:
                    print("BLACKJACK! No action needed")
                    return True
    return False

def advice(cards, dealer_card):
    sum = cards[0] + cards[1]
    if sum >= 17:
        print("STAND")
    elif sum >= 12:
        if dealer_card >= 7:
            print("HIT")
        else:
            print("STAND")
    elif sum == 11:
        if dealer_card != 11:
            print("DOUBLE")
        else:
            print("HIT")
    elif sum == 10:
        if dealer_card != 10 and dealer_card != 11:
            print("DOUBLE")
        else:
            print("HIT")
    elif sum == 9:
        if dealer_card >= 3 and dealer_card <= 6:
            print("DOUBLE")
        else:
            print("HIT")
    else:
        print("HIT")

def main():
    print(advice(get_cards(), get_dealer_card()))

if __name__ == "__main__":
    main()