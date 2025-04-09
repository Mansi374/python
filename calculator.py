def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

def exp(a, b):
    return a ** b

while True:
    print("Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "6":
        print("Exiting calculator.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print("Result:", exp(num1, num2))
    else:
        print("Invalid operation!")
