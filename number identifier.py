def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return n == sum(digit ** power for digit in digits)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

try:
    # Accept user input
    num = int(input("Enter an integer: "))

    # Check properties
    prime = is_prime(num)
    armstrong = is_armstrong(num)
    palindrome = is_palindrome(num)

    # Display results
    print(f"\nNumber: {num}")
    if prime:
        print("- It is a Prime number.")
    if armstrong:
        print("- It is an Armstrong number.")
    if palindrome:
        print("- It is a Palindrome number.")

    # If none of the conditions are met
    if not (prime or armstrong or palindrome):
        print("- It does not satisfy any of the given conditions.")

except ValueError:
    print("\nError: Please enter a valid integer.")
