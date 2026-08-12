def get_cards():
    cards = []
    amount = int(input("How many cards do you want to rank? "))
    print ("PS: Cards should be written in the format '(number/letter + initial of suit)'.")
    for i in range(amount):
        cards.append(input(f"Please enter card#{i+1}: ").upper())
    return cards

def seperate_value(cards):
    values = []
    suits = []
    for card in cards:
        values.append(int(card[:-1]))
        suits.append(card[-1])
    return values, suits

print(seperate_value(get_cards()))