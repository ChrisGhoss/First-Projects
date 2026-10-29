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

def main():
    print(get_cards())

if __name__ == "__main__":
    main()