try:
    # Accept two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display before swapping
    print(f"Before swapping: num1 = {num1}, num2 = {num2}")

    # Swap using tuple unpacking
    num1, num2 = num2, num1

    # Display after swapping
    print(f"After swapping: num1 = {num1}, num2 = {num2}")

except ValueError:
    print("Error: Please enter valid numeric values.")