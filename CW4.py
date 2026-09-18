students = {}

while 1:
    print("")
    print("[1] Add student")
    print("[2] Remove student")
    print("[3] Modify student")
    print("[4] Print students")
    print("[5] Exit")
    print("")
    UI = input("Input: ")

    if(UI == "1"):
        N = input("Enter student name: ")
        M = input("Enter student major: ")
        Y = input("Which year?: ")
        students.update({"S"+str(len(students)+1): {"Name": N, "Major": M, "Year":Y}})
        print(students)
    elif(UI == "2"):
        Sr = input("Enter student to remove: ")
        del students[Sr]
    elif(UI == "3"):
        SC = input("Which student to modify?: ")
        print("[1] Name, [2] Major, [3] Year")
        SM = input("What to modify?: ")
        if(SM == "1"):
            CN = input("Name to change to: ")
            students[SC]["Name"] = CN
        elif (SM == "2"):
            CM = input("Major to change to: ")
            students[SC]["Major"] = CM
        elif (SM == "3"):
            CY = input("change year to: ")
            students[SC]["Name"] = CY
    elif(UI == "4"):
        print(sudents)