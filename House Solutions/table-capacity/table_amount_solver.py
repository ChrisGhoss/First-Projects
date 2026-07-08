def get_guests():
    while True:
        try:
            amount = int(input("Enter the amount of guests for your table: "))
            if amount > 0:
                return amount
            else:
                print("Your integer should be positive!")
        except ValueError:
            print("Please enter a valid integer.")

def yes_or_no(text):
    print(text)
    while True:
        answer = input("Enter (yes/no): ").lower().strip()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")

def seat_edges():
    return yes_or_no("Do you want people sitting at the edges? ")

def summary():
    while True:
        guests = get_guests()
        s_edges = seat_edges()
        print("Summary:")
        print(f"Guests: {guests}")
        print(f"Seat Edges: {s_edges}")
        if yes_or_no("Are you sure you want to continue?") == "yes":
            return guests, s_edges
        
def table_length():
    space_per_person = 60
    amount_of_guests, uses_seat_edges = summary()
    if amount_of_guests == 1 or (uses_seat_edges == "yes" and amount_of_guests <= 4):
        return space_per_person
    if amount_of_guests % 2 == 1:
        amount_of_guests += 1
    if uses_seat_edges == "no":
        return (amount_of_guests / 2) * space_per_person
    else:
        return ((amount_of_guests - 2) / 2) * space_per_person

def main():
    length = table_length()
    print(f"Your table should be about {length}cm.")

if __name__ == "__main__":
    main()