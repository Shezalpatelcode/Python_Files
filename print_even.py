def print_even_numbers_recursive(current_number, end_number):
    # Base case: if the current number exceeds the end number, stop recursion.
    if current_number > end_number:
        return

    # Check if the current number is even.
    if current_number % 2 == 0:
        print(current_number, end=" ")  # Print the even number.

    # Recursive call: increment the current number and call the function again.
    print_even_numbers_recursive(current_number + 1, end_number)

# Example usage: print even numbers from 1 to 20
print_even_numbers_recursive(1, 20)