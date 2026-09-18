Courses = {}
L = []
while 1:
    print("")
    print("[1] Add a course")
    print("[2] Remove a course")
    print("[3] Replace a course")
    print("")
    UI = input("Input: ")
    if (UI == "1"):
        print("")
        UA = input("Name of course to add: ")
        Courses["Course"+str(len(Courses)+1)] = UA
        L += UA
        print(Courses)
        print(L)
    elif (UI == "2"):
        print("")
        print(Courses)
        print("")
        UR = input("What course to remove?: ")
        for i in range(len(L)):
            if L[i - 1] == Courses[UR]:
                del L[i - 1]
                print(L)
        del Courses[UR]
        Courses = {}
        for b in range(len(L)):
            Courses["Course"+str(b+1)] = L[b]
        print(Courses)
    elif (UI == "3"):
        print("")
        print(Courses)
        print("")
        UR = input("What course to replace?: ")
        NC = input("What course to replace it with?: ")
        if UR in Courses:
            Courses[UR] = NC
        else:
            print("Course not in dictonary!")
