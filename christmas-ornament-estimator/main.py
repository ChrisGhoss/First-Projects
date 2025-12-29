from math import sqrt, pi

def ornament_estimator(budget, height, radius):
    # Formula that calculates the surface of a cone
    slant_height = sqrt(radius**2 + height**2)
    surface = pi * radius * slant_height
    # Checks the budget
    if budget == "yes":
        # Budget present means less ornaments per meter square
        base_ornament = surface * 8
    elif budget == "no":
        # Budget absent means more ornaments per meter square
        base_ornament = surface * 12
    else:
        return
    total_ornament = round(base_ornament)
    print(f"About {total_ornament} ornaments are needed for your Christmas tree!")
    return total_ornament
    

def user_input():
    # Asks the user for all necessary information
    budg = input("Are you on a budget? (yes/no): ")
    print("All measures are in meters")
    h = float(input("Enter the height of your tree: "))
    r = float(input("Enter the radius of your tree: "))
    return budg, h, r

# Combines both functions to call only the main one
def main():
    budg1, h1, r1 = user_input()
    ornament_estimator(budg1, h1, r1)

main()