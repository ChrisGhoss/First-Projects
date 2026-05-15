from math import ceil

def get_dimensions():
    print("Please note: All measures should be in meters.")
    return dim_input("height"), dim_input("length"), dim_input("width")

def dim_input(unit):
    while True:
        try:
            ans = float(input(f"Please enter the {unit} of your room: "))
        except ValueError:
            print(f"Please enter a valid float for the {unit}.")
        return ans

def area_of_room(h, l, w):
    return (2 * l * h) + (2 * w * h)

def area_w_ceiling(h, l, w):
    return area_of_room(h, l, w) + (l * w)

def get_paint(area, quality):
    if quality == "yes":
        premium_rate = 12
        return ceil(area / premium_rate)
    else:
        standard_rate = 8
        return ceil(area / standard_rate)

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

def main():
    h, l, w = get_dimensions()
    ans_ceiling = yes_or_no("Will you paint the ceiling?")
    if ans_ceiling == "yes":
        user_area = area_w_ceiling(h, l, w)
    else:
        user_area = area_of_room(h, l, w)
    user_quality = yes_or_no("Do you have premium cans?")
    print(f"The total amount of paint cans is {get_paint(user_area, user_quality)}")
    
if __name__ == "__main__":
    main()
