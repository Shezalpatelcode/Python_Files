# Function to calculate the number of notes using switch-case like logic
def count_notes(amount, denomination):
    denominations = [100, 50, 20, 10, 5, 2, 1]
    
    # Find the index to start from the given denomination
    try:
        start_index = denominations.index(denomination)
    except ValueError:
        print("Invalid denomination entered!")
        return

    match denomination:
        case 100:
            start = denominations[0:]
        case 50:
            start = denominations[1:]
        case 20:
            start = denominations[2:]
        case 10:
            start = denominations[3:]
        case 5:
            start = denominations[4:]
        case 2:
            start = denominations[5:]
        case 1:
            start = denominations[6:]
        case _:
            print("Invalid denomination!")
            return

    # Calculate and print notes count
    for d in start:
        notes = amount // d
        amount = amount % d
        print(f"{d} rupees note: {notes}")


# ---------- Main Program ----------
amount = int(input())
denomination = int(input())

count_notes(amount, denomination)
