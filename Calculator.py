# demo a basic calculator using conditional statmemtes and functions
def input_numbers():
    try:
        first_no = float(input("enter the first no : "))
        second_no = float(input("enter the second no : "))
        status = int(input("Pls enter 1 for addition, 2 for substraction, 3 for multiplication, 4 for division"))
    except ValueError:
        print("enter a valid number")
        input_numbers()
    return first_no, second_no, status

def add(first_no, second_no):
    result = first_no+second_no
    print(result)

def subtract(first_no, second_no):
    result = first_no - second_no
    print(result)

def multiply(first_no, second_no):
    result = first_no*second_no
    print(result)

def division(first_no, second_no):
    if (second_no!=0):
        result=first_no/second_no
        print(result)
    else:
        print("Pls enter a valid No. you cannot deivide by Zero")

def main(response):
    first_no=response[0]
    second_no=response[1]
    status=response[2]

    if (status==1):
        add(first_no, second_no)
    elif (status==2):
        subtract(first_no, second_no)
    elif (status==3):
        multiply(first_no, second_no)
    elif (status==4):
        division(first_no, second_no)
    else:
        print("Pls enter a vlaid number")

res = input_numbers()
main(res)