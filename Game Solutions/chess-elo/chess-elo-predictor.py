def get_player_elo(number):
    while True:
        try:
            value = float(input(f"Please enter P{number}'s elo: "))
            if value > 0:
                return value
            else:
                print("Your elo should be positive!")
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

def get_k_factor(elo):
    if elo < 1600:
        return 40
    elif elo < 2400:
        return 20
    else:
        return 10

def formula():
    elo1 = get_player_elo(1)
    elo2 = get_player_elo(2)
    dif = elo2 - elo1
    expected = 1/(1 + 10**(dif/400))
    score, result = get_result()
    k = get_k_factor(elo1)
    return elo1 + k * (score - expected), result

def main():
    new_elo, result = formula()
    print(f"P1 will have {new_elo} elo if they {result}.")

if __name__ == "__main__":
    main()