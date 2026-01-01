from math import sqrt, pi

def ornament_estimator(budget, height, radius):
    # Formula that calculates the surface of a cone
    slant_height = sqrt(radius**2 + height**2)
    surface = pi * radius * slant_height
    # Checks the budget
    if budget == "yes":
        # Budget present means less ornaments per meter square
        ornaments_per_ms = 8
    elif budget == "no":
        # Budget absent means more ornaments per meter square
        ornaments_per_ms = 12
    # Calculates the amount according to the surface and the ornament rate
    base_ornament = surface * ornaments_per_ms
    total_ornament = round(base_ornament)
    print(f"About {total_ornament} ornaments are needed for your Christmas tree!")
    return total_ornament
    
# Asks the user for all necessary information
def user_input():
    # Checks if the budget input is either "yes" or "no"
    budg = yes_or_no("Are you on a budget?")
    print("Please note: All measures should be in meters.")
    # Checks if the height input is a valid float
    while True:
        try:
            h = float(input("Enter the height of your tree: "))
            break
        except ValueError:
            print("Please enter a valid float for your tree height.")
    # Checks if the radius input is a valid float
    while True:
        try:
            r = float(input("Enter the radius of your tree: "))
            break
        except ValueError:
            print("Please enter a valid float for your tree radius.")
    return budg, h, r

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

# Combines all necessary functions to only call the main one
def main():
    while True:
        budg1, h1, r1 = user_input()
        print("Summary:")
        print(f"Budget: {budg1}")
        print(f"Height: {h1}")
        print(f"Radius: {r1}")
        v1 = yes_or_no("Are you sure you want to continue?")
        if v1 == "yes":
            break
    ornament_estimator(budg1, h1, r1)
    return

main()