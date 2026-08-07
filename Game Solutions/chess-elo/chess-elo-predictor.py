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
        result = input("Which result are you expecting for P1 (W/D/L)? ").lower().strip()
        if result in ("w", "win"):
            return 1, 0, "win", "lose"
        elif result in ("d", "draw"):
            return 0.5, 0.5, "draw", "draw"
        elif result in ("l", "loss"):
            return 0, 1, "lose", "win"
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
        score1, score2, result1, result2 = get_result()
        print("Summary:")
        print(f"P1's Elo: {Elo1}")
        print(f"P2's Elo: {Elo2}")
        print(f"Result for P1: {result1}")
        print(f"Result for P2: {result2}")
        if yes_or_no("Are you sure you want to continue?") == "yes":
            return Elo1, Elo2, score1, score2, result1, result2

def formula():
    Elo1, Elo2, score1, score2, result1, result2 = summary()
    dif1 = Elo2 - Elo1
    dif2 = Elo1 - Elo2
    expected1 = 1/(1 + 10**(dif1/400))
    expected2 = 1/(1 + 10**(dif2/400))
    k1 = get_k_factor(Elo1)
    k2 = get_k_factor(Elo2)
    return Elo1 + k1 * (score1 - expected1), Elo2 + k2 * (score2 - expected2), result1, result2

def main():
    new_Elo1, new_Elo2, result1, result2 = formula()
    print(f"P1 will have {round(new_Elo1)} Elo if they {result1}.")
    print(f"P2 will have {round(new_Elo2)} Elo if they {result2}.")

if __name__ == "__main__":
    main()