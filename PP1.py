EName = input("Enter Employee's Name: ")
EPay = int(input("Enter Employee's basic pay: "))
PDed = int(input("Enter Employee's pay deduction: "))
TotalP = EPay - PDed
print("Employee:",EName+"   Pay: $"+ str(TotalP))