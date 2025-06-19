def input_numbers():
    first_no = float(input("enter the first no : "))
    second_no = float(input("enter the second no : "))
    return first_no, second_no

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# This block ensures the code below only runs when executing Calculator.py directly
if __name__ == "__main__":
    respo = input_numbers()
    print("Addition:", add(*respo))
    print("Subtraction:", subtract(*respo))
    print("Multiplication:", multiply(*respo))
    print("Division:", divide(*respo))
