Number1 = int(input("Enter Number1: "))
Number2 = int(input("Enter Number2: "))
Number3 = int(input("Enter Number3: "))

if Number1 > Number2 and Number1 > Number3:
    print("Number1 is the biggest")

if Number2 > Number3 and Number2 > Number1:
    print("Number2 is the biggest")

if Number3 > Number1 and Number3 > Number2:
    print("Number3 is the biggest")
