print("Welcome to Calculator")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero not possible."
    return x / y

print("Select operator to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

perform = input("Enter choice: ")

if perform in ['1', '2', '3', '4']:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    if perform == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif perform == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif perform == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif perform == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid operation,try again!.")
