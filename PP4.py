Num = int(input("Input a number to multiply: "))
MT = int(input("How many times?: "))
for i in range(1, MT + 1):
    Ans = Num * i
    print(str(Num)+" X "+str(i)+" = "+str(Ans))