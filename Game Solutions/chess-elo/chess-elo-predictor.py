def get_player_Elo(number):
    while True:
        try:
            value = float(input(f"Please enter P{number}'s Elo: "))
            if value > 0:
                return value
            else:
                print("Your Elo should be positive!")
        except ValueError:
            print("Please enter a valid float.")

def get_result():
    while True:
        result = input("Which result are you expecting (W/D/L)? ")
        if result in ("W", "w", "win"):
            return 1, "win"
        elif result in ("D", "d", "draw"):
            return 0.5, "draw"
        elif result in ("L", "l", "loss"):
            return 0, "lose"
        else:
            print("Please enter W, D or L")

def get_k_factor(Elo):
    if Elo < 1600:
        return 40
    elif Elo < 2400:
        return 20
    else:
        return 10

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

def summary():
    while True:
        Elo1, Elo2 = get_player_Elo(1), get_player_Elo(2)
        score, result = get_result()
        print("Summary:")
        print(f"P1's Elo: {Elo1}")
        print(f"P2's: {Elo2}")
        print(f"Result: {result}")
        if yes_or_no("Are you sure you want to continue?") == "yes":
            return Elo1, Elo2, score, result

def formula():
    Elo1, Elo2, score, result = summary()
    dif = Elo2 - Elo1
    expected = 1/(1 + 10**(dif/400))
    k = get_k_factor(Elo1)
    return Elo1 + k * (score - expected), result

def main():
    new_Elo, result = formula()
    print(f"P1 will have {round(new_Elo)} Elo if they {result}.")

if __name__ == "__main__":
    main()