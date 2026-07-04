def get_answer(text, type):
    while True:
        try:
            if type == "integer":
                value = int(input(text))
            elif type == "float":
                value = float(input(text))
            if value > 0:
                return value
            else:
                print(f"Your {type} should be positive!")
        except ValueError:
            print(f"Please enter a valid {type}.")

def get_wall_width():
    return get_answer("Enter the width of your wall: ", "float")

def get_frame_number():
    return get_answer("Enter the amount of frames: ", "integer")

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

def get_frame_width(frame_number):
    if frame_number > 1:
        ans = yes_or_no("Are all your frames the same size? ")
        if ans == "yes":
            return get_answer("Enter the common width of your frame: ", "float") * frame_number
        elif ans == "no":
            total = 0
            for i in range(frame_number):
                total += get_answer(f"Enter the width of frame #{i+1}: ", "float")
            return total
    elif frame_number == 1:
        return get_answer("Enter the width of the frame: ", "float")

def verification():
    wall = get_wall_width()
    amount = get_frame_number()
    total_frame_width = get_frame_width(amount)
    return wall, amount, total_frame_width

def summary():
    while True:
        wall, amount, total_frame_width = verification()
        print("Summary:")
        print(f"Wall Width: {wall}")
        print(f"Frame Amount: {amount}")
        print(f"Total Frame Width: {total_frame_width}")
        if yes_or_no("Are you sure you want to continue?") == "yes":
            return wall, amount, total_frame_width
    
def main():
    print("PS: Measure should be in centimeters (cm).")
    wall, amount, total_frame_width = summary()
    gaps = amount + 1
    space = (wall - total_frame_width) / (gaps)
    print(f"The amount of space in each gap should be about {space}cm.")

if __name__ == "__main__":
    main()