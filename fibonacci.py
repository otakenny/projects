def generate_fibonacci(n):
    fib_sequence = [0, 1]  # Start with first two terms
    for _ in range(n - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]  # Return only the first n terms

try:
    # Accept user input
    n = int(input("Enter a positive integer for Fibonacci sequence: "))

    # Validate input
    if n <= 0:
        print("Error: Please enter a positive integer greater than zero.")
    else:
        # Generate and display Fibonacci sequence
        fibonacci_numbers = generate_fibonacci(n)
        print("Fibonacci Sequence:", fibonacci_numbers)

except ValueError:
    print("Error: Invalid input! Please enter a valid positive integer.")

