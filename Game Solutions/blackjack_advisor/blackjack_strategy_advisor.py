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
    print("Input should be an integer from 1 to 10")
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
    if cards[0] + cards[1] == 21:
        print("Blackjack! No action needed")
        
def main():
    print(get_dealer_card())

if __name__ == "__main__":
    main()