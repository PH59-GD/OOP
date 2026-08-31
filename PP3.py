SName = input("Enter student name: ")
C1 = int(input("Enter course1 grade: "))
C2 = int(input("Enter course2 grade: "))
C3 = int(input("Enter course3 grade: "))
Total = C1 + C2 + C3

Percent = (Total/300)*100
if(Percent <= 0):
    Percent = 0
if(Percent >= 90 and Percent <= 100):
    print(SName+"'s grade is: A")
elif(Percent >= 80 and Percent < 90):
    print(SName+"'s grade is: B")
elif(Percent >= 70 and Percent < 80):
    print(SName+"'s grade is: C")
elif(Percent >= 60 and Percent < 70):
    print(SName+"'s grade is: D")
elif(Percent >= 0 and Percent < 60):
    print(SName+"'s grade is: F")
#print(Percent)