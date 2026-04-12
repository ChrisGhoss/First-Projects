from sys import exit

def inside_temp(outside_temp):
    if outside_temp <= 18:
        return(cold_to_hot(outside_temp))
    else:
        return(hot_to_cold(outside_temp))

def get_outside_temp():
    while True:
        try:
            temp = float(input("Enter your outside temperature (°C): "))
            if -90 <= temp <= 57:
                if not(18 < temp < 25):
                    break
                else:
                    print("Perfect! You don't need an air conditioner.")
                    ans = yes_or_no("Would you like to change it?")
                    if ans == "no":
                        exit("You're all set!")
            else:
                print("Temperature is not realistic.")
        except ValueError:
            print("Please enter a valid float for the outside temperature.")
    return temp

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

def cold_to_hot(temp):
    # Integer found at 25°C
    initial_int = 20
    # Linear function : Higher outside temp = Less inside temp
    optimal_temp = initial_int - (temp*0.1)
    return optimal_temp

def hot_to_cold(temp):
    # Integer found at 18°C
    initial_int = 28.6
    # Linear function : Higher outside temp = Less inside temp
    optimal_temp = initial_int - (temp*0.15)
    return optimal_temp

def main():
    temp = get_outside_temp()
    print(f"Your inside temperature should be about {inside_temp(temp)}°C")

if __name__ == "__main__":
    main()