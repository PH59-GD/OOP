List = []
while 1:
    print("")
    print("Your list has: "+str(len(List))+" Items.")
    print("")
    print("[1] Add to list")
    print("[2] Remove from list")
    print("[3] Replace in list")
    print("[4] sort the list")
    print("[5] Print the list")
    print("[6] Exit")
    print("")
    UI = input("Input: ")
    if UI == "1":
        print("")
        UIA = int(input("How many items to add?: "))
        for i in range(UIA):
            UA = int(input("What to add?: "))
            List.append(UA)
    elif UI == "2":
        print("")
        UIA = int(input("How many items to remove?: "))
        for i in range(UIA):
            UR = int(input("What to remove?: "))
            if (UR in List):
                List.remove(UR)
            else:
                print("Item not in list!")
    elif UI == "3":
        print("")
        UR = int(input("What to Replace?: "))
        URP = int(input("What to Replace it with?: "))
        if UR not in List:
            print("")
            print("Item not in list!")
        for i in range(len(List)):
            if(List[i] == UR):
                List[i] = URP
    elif UI == "4":
        List.sort()
        print("List sorted.")
    elif UI == "5":
        print("")
        print(List)
    elif UI == "6":
        break


