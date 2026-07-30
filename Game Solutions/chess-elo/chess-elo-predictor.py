def get_player_elo(number):
    return int(input(f"Please enter P{number}'s elo: "))

def get_result():
    result = input("Which result are you expecting (W/D/L)? ")
    if result == "W":
        return 1, "win"
    elif result == "D":
        return 0.5, "draw"
    elif result == "L":
        return 0, "lose"

def formula():
    elo1 = get_player_elo(1)
    elo2 = get_player_elo(2)
    dif = elo2 - elo1
    expected = 1/(1 + 10**(dif/400))
    score, result = get_result()
    k = 32
    return elo1 + k * (score - expected), result

def main():
    new_elo, result = formula()
    print(f"Player1 will have {new_elo} elo if they {result}.")

if __name__ == "__main__":
    main()