#Functions - piece of code that does something specific
# Examples of functions
#input()
#print()
#exit()
#Function call Add() - - - - > Called Function
#User defined function:
def add(A, B):
    Sum = Num1 + Num2
    return print(str(Num1) +" + "+str(Num2) +" = "+ str(Sum))
def subtract(A, B):
    Answer = Num1 - Num2
    return print(str(Num1) + " - " + str(Num2) + " = " + str(Answer))
def divide(A, B):
    Answer = Num1 / Num2
    return print(str(Num1) + " / " + str(Num2) + " = " + str(Answer))
def multiply(A, B):
    Answer = Num1 * Num2
    return print(str(Num1) + " * " + str(Num2) + " = " + str(Answer))
while 1:
    print("")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] divide")
    print("[4] Multiply")
    print("[5] Exit")
    print("")
    UC = input("Input: ")
    print("")
    if UC == "5":
        print("Exiting...")
        break
    Num1 = int(input("Enter number 1: "))
    Num2 = int(input("Enter number 2: "))
    if UC == "1":
        add(Num1, Num2)
    elif UC == "2":
        subtract(Num1, Num2)
    elif UC == "3":
        divide(Num1, Num2)
    elif UC == "4":
        multiply(Num1, Num2)
