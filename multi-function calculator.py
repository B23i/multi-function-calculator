def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Result:", result)

def subtract_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))          
    result = num1 - num2
    print("Result:", result)

def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("Result:", result)

def divide_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)

def calculate_square():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 ** num2
    print("Square:", result)

print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Calculate Square")

choice = input("Enter your choice (1-5): ")
if choice == "1":
    add_numbers()
elif choice == "2":
    subtract_numbers()
elif choice == "3":
    multiply_numbers()
elif choice == "4":
    divide_numbers()
elif choice == "5":
    calculate_square()
else:
    print("Invalid choice")

