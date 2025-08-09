# Simple Calculator

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take operation input from user
choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1':
    result = num1 + num2
    operation = "+"
elif choice == '2':
    result = num1 - num2
    operation = "-"
elif choice == '3':
    result = num1 * num2
    operation = "*"
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = "/"
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid input! Please select a valid operation.")
    exit()

# Display the result
print(f"\nResult: {num1} {operation} {num2} = {result}")
