# Prompt the user to input the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to input the second number
num2 = float(input("Enter the second number: "))

# Perform addition
addition = num1 + num2

# Perform subtraction
subtraction = num1 - num2

# Perform multiplication
multiplication = num1 * num2

# Perform division and handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Print the results with descriptive messages
print(f"Addition of {num1} and {num2} is: {addition}")
print(f"Subtraction of {num1} from {num2} is: {subtraction}")
print(f"Multiplication of {num1} and {num2} is: {multiplication}")
print(f"Division of {num1} by {num2} is: {division}")
