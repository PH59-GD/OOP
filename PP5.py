while (True):
    print("")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] EXIT")
    print("")
    UC = input("Enter a number for an operation: ")
    if UC == "5":
        print("Exiting...")
        break
    Num1 = int(input("Enter number 1: "))
    Num2 = int(input("Enter number 2: "))
    if UC == "1":
        Ans = Num1 + Num2
        print(str(Num1)+" + "+str(Num2)+" = "+ str(Ans))
    elif UC == "2":
        Ans = Num1 - Num2
        print(str(Num1) + " - " + str(Num2) + " = " + str(Ans))
    elif UC == "3":
        Ans = Num1 * Num2
        print(str(Num1) + " * " + str(Num2) + " = " + str(Ans))
    elif UC == "4":
        Ans = Num1 / Num2
        print(str(Num1) + " / " + str(Num2) + " = " + str(Ans))