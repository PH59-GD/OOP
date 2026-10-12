# classes - objects - OOADP - Python
# *.txt  #text storage
# *.dat  #object
import pickle
class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.advisor = ""
        self.Dict = {}

    def create_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter student department: ")
        self.Dict["student"] = {"Name": self.name, "ID": self.id, "Department": self.department,
                                "Advisor": self.advisor}

    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Advisor:", self.advisor)




s1 = Student()
s1.create_student()
#s1.display_student()

file1 = open("mystudents.dat", "ab")
pickle.dump(s1, file1)
file1.close()

file2 = open("mystudents.dat", "rb")

while True:
    try:
        data = pickle.load(file2)
        print(data.name)
        print(data.id)
        print(data.department)

    except(EOFError):
        break
file2.close()









































'''
file1 = open("mytext.txt", "w")

file1.writelines(input("Enter your name: "))
file1.writelines(" this is Monday.")
file1.writelines(" How are you?")
file1.close()

file2 = open("mytext.txt", "r")
a_word = input()
for line in file2:
    if a_word in line:
        print(line)

file2.close()
'''