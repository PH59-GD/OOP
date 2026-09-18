Courses = {}
L = []
while 1:
    print("")
    print("[1] Add a course")
    print("[2] Remove a course")
    print("[3] Replace a course")
    print("[4] Print")
    print("[5] Exit")
    print("")
    UI = input("Input: ")
    if (UI == "1"):
        print("")
        UA = input("Name of course to add: ")
        Courses["Course"+str(len(Courses)+1)] = UA
        L.append(UA)
    elif (UI == "2"):
        UR = input("What course to remove?: ")
        if(UR not in Courses.keys()):
             print("Cannot remove item! Not in dictonary!")
        for i in range(len(L)):
            if L[i - 1] == Courses[UR]:
                del L[i - 1]
        Courses = {}
        for b in range(len(L)):
            Courses["Course"+str(b+1)] = L[b]
        print(Courses)
    elif (UI == "3"):
        UR = input("What course to replace?: ")
        NC = input("What course to replace it with?: ")
        if UR in Courses.keys():
            Courses[UR] = NC
        else:
            print("Course not in dictonary!")
        print(Courses)
    elif (UI == "4"):
        print(Courses)
    elif (UI == "5"):
        break