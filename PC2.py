import time
Number1 = int(input("Enter Number1: "))
Number2 = int(input("Enter Number2: "))
Number3 = int(input("Enter Number3: "))

if Number1 > Number2 and Number1 > Number3:
    print("Number1 is the biggest")

elif Number2 > Number3 and Number2 > Number1:
    print("Number2 is the biggest")

elif Number3 > Number1 and Number3 > Number2:
    print("Number3 is the biggest")

if Number1 < Number2 and Number1 < Number3:
    print("Number1 is the smallest")

elif Number2 < Number3 and Number2 < Number1:
    print("Number2 is the smallest")

elif Number3 < Number1 and Number3 < Number2:
    print("Number3 is the smallest")

time.sleep(60)
