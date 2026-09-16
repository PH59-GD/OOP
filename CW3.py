Courses = {}

while 1:
    print("")
    print("[1] Add a course")
    print("[2] Remove a course")
    print("[3] Replace a course")
    print("")
    UI = input("Input: ")
    if (UI == "1"):
        UA = input("Name of course to add: ")
        Courses["Course"+str(len(Courses)+1)] = [UA]
        print(Courses)
    if (UI == "2"):
        print(Courses.keys())
        UR = input("What course to remove?: ")
        
