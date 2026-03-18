from math import sqrt, pi

def ornament_estimator(budget, height, radius):
    slant_height = sqrt(radius**2 + height**2)
    # Formula that calculates the surface of a cone
    surface = pi * radius * slant_height
    rates = {"yes": 8, "no": 12}
    ornaments_per_ms = rates[budget]
    # Formula is based on the surface + ornament rate
    total_ornament = round(surface * ornaments_per_ms)
    print(f"About {total_ornament} ornaments are needed for your Christmas tree!")
    return total_ornament
    
def user_input():
    budg = yes_or_no("Are you on a budget?")
    print("Please note: All measures should be in meters.")
    h = get_float("height")
    r = get_float("radius")
    return budg, h, r

def get_float(unit):
    while True:
        try:
            u = float(input(f"Enter the {unit} of your tree: "))
            if u > 0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print(f"Please enter a valid float for your tree {unit}.")
    return u

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

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

if __name__ == "__main__":
    main()
