#Putting Objects into Class (template) Abstraction
# List of students' Names
mystudents = [] #Store student objects
class Student:
    def __init__(self): #Constuctor
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter student department: ")
    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)

#stu = Student()
#stu.create_new_student()
#stu.display_student()
#mystudents.append(stu)

class Faculty:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.Num_students = ""
        self.course = ""
        self.course_Des = ""
    def create_new_faculty(self):
        self.name = input("Enter faculty name: ")
        self.department = input("Enter faculty department: ")
        self.Num_students = input("Enter number of faculty's students: ")
    def display_student(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Number of current students:", self.Num_students)
    def create_Courses(self):
        self.course = input("Enter Course name: ")
        self.course_Des = input("Enter Course description: ")
    

