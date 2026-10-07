#Putting Objects into Class (template) Abstraction
# List of students' Names
mystudents = [] #Store student objects
myfaculty = []
mycourses = []
class Student:
    def __init__(self): #Constuctor
        self.id = ""
        self.name = ""
        self.department = ""
        self.advisor = ""
        self.Dict = {}
    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter student department: ")
        self.Dict["student"] = {"Name": self.name, "ID": self.id, "Department": self.department, "Advisor": self.advisor}
    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Advisor:", self.advisor)
    def assign_advisor(self):
        print(myfaculty)
        CF = int(input("Enter advisors Faculty ID number: "))
        self.Dict["student"] = {"Name": self.name, "ID": self.id, "Department": self.department, "Advisor": self.advisor}
        self.advisor = myfaculty[CF].name
class Faculty:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.id = ""
        self.Courses = {}
    def create_new_faculty(self):
        self.name = input("Enter faculty name: ")
        self.department = input("Enter faculty department: ")
        self.id = input("Enter faculty's ID: ")
    def display_faculty(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Faculty ID:", self.id)
class Courses:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.credits = ""
        self.students = []
    def create_Courses(self):
        self.name = input("Enter Course name: ")
        self.department = input("Enter course department: ")
        self.credits = input("Enter Course credits: ")
    def display_courses(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Course credits:", self.credits)
        print("Course students: ", self.students)
    def register_students(self):
        print(mystudents)
        SC = int(input("Enter student to add to course(Index Number): "))
        self.students.append(mystudents[SC].Dict["student"]["ID"])
while True:
    print("")
    print("[1] Student")
    print("[2] Faculty")
    print("[3] Courses")
    print("")
    UC = input("Input: ")
    if(UC == "1"):
        while True:
            print("")
            print("[1] Add student")
            print("[2] Display student")
            print("[3] Assign advisor")
            print("[4] Back")
            print("")
            UC = input("Input: ")
            if(UC == "1"):
                AT = int(input("How many courses to add?: "))
                for i in range(AT):
                    Student = Student()
                    Student.create_new_student()
                    mystudents.append(Student)
            elif(UC == "2"):
                SC = int(input("What Student?(Index Number): "))
                mystudents[SC].display_student()
                #print(mystudents[0].Dict)
            elif(UC == "3"):
                print(mystudents)
                SC = int(input("What student?(Index Number): "))
                mystudents[SC].assign_advisor()
            elif(UC == "4"):
                break
    elif(UC == "2"):
        while True:
            print("")
            print("[1] Add faculty")
            print("[2] Display faculty")
            print("[3] Back")
            print("")
            UC = input("Input: ")
            if(UC == "1"):
                AT = int(input("How many courses to add?: "))
                for i in range(AT):
                    Faculty = Faculty()
                    Faculty.create_new_faculty()
                    myfaculty.append(Faculty)
            elif(UC == "2"):
                SC = int(input("What faculty(Index Number)?: "))
                myfaculty[SC].display_faculty()
                #print(mystudents[0].Dict)
            elif(UC == "3"):
                break
    elif(UC == "3"):
        while True:
            print("")
            print("[1] Add course")
            print("[2] Display courses")
            print("[3] Register students")
            print("[4] Back")
            print("")
            UC = input("Input: ")
            if(UC == "1"):
                AT = int(input("How many courses to add?: "))
                for i in range(AT):
                    Courses = Courses()
                    Courses.create_Courses()
                    mycourses.append(Courses)
            elif(UC == "2"):
                SC = int(input("What Course?(Index Number): "))
                mycourses[SC].display_courses()
                #print(mystudents[0].Dict)
            elif(UC == "3"):
                print(mystudents)
                SC = int(input("What course?(Index Number): "))
                mycourses[SC].register_students()
            elif(UC == "4"):
                break