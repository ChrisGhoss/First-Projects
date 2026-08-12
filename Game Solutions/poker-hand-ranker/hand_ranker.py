from collections import Counter

def get_cards():
    cards = []
    print ("PS: Cards should be written in the format '(number/letter + initial of suit)'.")
    for i in range(5):
        cards.append(input(f"Please enter card#{i+1}: ").upper())
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

def main():
    values, suits = seperate_value(get_cards())