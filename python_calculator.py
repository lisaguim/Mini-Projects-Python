#MiniProject_1 Code: Python Calculator

print("\n********Python  Calculator**********")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("\nChoice the number of the desired operation: \n")
print("1 - Sum")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = input("\nEnter your option number: ")

num1 = int(input("Enter the first number that will be used in the operation "))
num2 = int(input("Enter the second number that will be used in the operation"))

if choice == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif choice == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif choice == '3':
    print("\n")
    print(num1, "x", num2, "=", multiply(num1, num2))
    print("\n")

elif choice == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

else:
    print("\nInvalid Option!")

