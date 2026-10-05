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
    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter student department: ")
    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Advisor:", self.advisor)
    def assign_advisor(self):
        print(myfaculty)
        CF = input("Enter advisors Faculty ID number: ")
        self.advisor = myfaculty[0]
stu = Student()
stu.create_new_student()
#stu.display_student()
mystudents.append(stu)

class Faculty:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.id = ""
    def create_new_faculty(self):
        self.name = input("Enter faculty name: ")
        self.department = input("Enter faculty department: ")
        self.id = input("Enter faculty's ID: ")
    def display_faculty(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Faculty ID:", self.id)
Fac = Faculty()
Fac.create_new_faculty()
#Fac.display_faculty()
myfaculty.append(Fac)

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
        SC = input("Enter student ID to add to course: ")
        self.students.append(mystudents[0])
Cou = Courses()
Cou.create_Courses()
#Cou.display_Courses()
mycourses.append(Cou)
mystudents[0].assign_advisor()
print(mystudents[0])
mycourses[0].register_students()
mycourses[0].display_courses()
mystudents[0].display_student()
myfaculty[0].display_faculty()
'''
while True:
    print("")
    print("[1] Student")
    print("[2] Faculty")
    print("[3] Courses")
    print("")
    if()
'''