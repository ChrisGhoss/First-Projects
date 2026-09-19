from collections import Counter

def get_cards():
    l_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    l_suits = ["C", "D", "H", "S"]
    cards = []
    print ("PS: Cards should be written in the format '(number [2-14] + suit initial [C-D-H-S])'.")
    for i in range(5):
        while True:
            card = input(f"Please enter card#{i+1}: ").upper()
            num_part = card[:-1]
            suit_part = card[-1:]
            if num_part not in l_numbers:
                print("Invalid, number should be from 2 to 14.")
                continue
            if suit_part not in l_suits:
                print("Invalid, suit should be either C, D, H or S.")
                continue
            if card not in cards:
                cards.append(card)
                break
            else:
                print("Card already in hand.")
    return cards

def seperate_value(cards):
    values = []
    suits = []
    for card in cards:
        values.append(int(card[:-1]))
        suits.append(card[-1])
    return sorted(values, reverse=True), suits

def is_flush(l_suits):
    for i in range(4):
        if l_suits[i] != l_suits[i+1]:
            return False
    return True

def is_straight(l_values):
    for i in range(4):
        if (l_values[i] - l_values[i+1]) != 1:
            return False
    return True

def get_value_count(l_values):
    counts = Counter(l_values)
    return sorted(list(counts.values()), reverse=True)

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")
        
def summary():
    while True:
        card_hand = get_cards()
        print("Summary:")
        for i in range(5):
            print(f"Card#{i+1}: {card_hand[i]}")
        if yes_or_no("Are you sure you want to continue?") == "yes":
            return card_hand

def main():
    cards = summary()
    values, suits = seperate_value(cards)
    straight = is_straight(values)
    flush = is_flush(suits)
    count = get_value_count(values)
    if straight and flush and values[0] == 14:
            print("ROYAL FLUSH")
    elif straight and flush:
        print("STRAIGHT FLUSH")
    elif count[0] == 4:
        print("FOUR OF A KIND")
    elif count[0] == 3 and count[1] == 2:
        print("FULL HOUSE")
    elif flush:
        print("FLUSH")
    elif straight:
        print("STRAIGHT")
    elif count[0] == 3:
        print("THREE OF A KIND")
    elif count[0] == 2 and count[1] == 2:
        print("TWO PAIR")
    elif count[0] == 2:
        print("PAIR")
    else:
        print("HIGH CARD")

if __name__ == "__main__":
    main()