
Number1 = int(input("Enter number1: "))
Operator = input("Enter the operator: ")
Number2 = int(input("Enter Number2: "))

if (Operator == "+"):
    A = Number1 + Number2
    print(A)
elif (Operator == "-"):
    A = Number1 - Number2
    print(A)
elif (Operator == "*"):
    A = Number1 * Number2
    print(A)
elif (Operator == "/"):
    if(Number2 >= Number1):
        A = Number1 / Number2
        print(A)
    else:
        print("Zero division ERROR!!")
else:
    print("ERROR invalid operator!!")