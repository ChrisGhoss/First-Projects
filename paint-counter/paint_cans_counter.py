from math import ceil

def get_dimensions():
    print("PS: All measures should be in meters (m)")
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
    return calculate_area(h, l, w) + (l * w)

def get_paint(area, quality):
    if quality == "Premium":
        premium_rate = 12
        return ceil(area / premium_rate)
    else:
        standard_rate = 8
        return ceil(area / standard_rate)

def main():
    ...