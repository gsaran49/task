def sum_of_digits(n: int):
    return sum(int(digit) for digit in str(abs(n)))

while True:
    user_input = input("Enter a number: ")

    if not user_input:
        print("Input cannot be null or empty. Please enter a valid number.")
    else:
        try:
            n = int(user_input)
            result = sum_of_digits(n)
            print(f"Sum of digits: {result}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
