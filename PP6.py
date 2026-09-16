#Sets, Tuples Self-Study
Dictonary = {"Name1": "Payton", "Name2": "Jim", "Name3": "Joe" } #record
#Dictonary = {}
Dictonary.update({"Name4": "Jemi"}) #Adding
Dictonary.update({"Name5": "Tim"})
del Dictonary["Name2"] #Removing
del Dictonary["Name3"]
Dictonary["Name4"] = "Melba" #Replacing
print(Dictonary)
print("")
Fullname = input("Enter your full name:  ")

Dictonary.update({"Name5": Fullname})
print(Dictonary)
